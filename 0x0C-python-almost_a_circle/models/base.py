import json

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            s = json.dumps(list_dictionaries)
            return s

    @classmethod
    def save_to_file(cls, list_objs):
        with open('{}.json'.format(cls.__name__), mode='w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                myList = []
                for i in list_objs:
                    i = i.to_dictionary()
                    myList.append(i)
                    f.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = None
        if cls.__name__ == 'Rectangle':
            dummy = cls(dictionary['width'], dictionary['height'])
            dummy.update(**dictionary)
        elif cls.__name__ == 'Square':
            dummy = cls(dictionary['size'])
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                my_list = cls.from_json_string(file.read())
        except IOError:
            my_list = []

        final_list = []
        for item in my_list:
            obj = cls.create(**item)
            final_list.append(obj)
        return final_list

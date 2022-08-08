from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        count = 1
        if args:
            for arg in args:
                if count == 1:
                    self.id = arg
                if count == 2:
                    self.size = arg
                if count == 3:
                    self.x = arg
                if count == 4:
                    self.y = arg
                count += 1

        else:
            if kwargs:
                for key in kwargs:
                    if key == 'id':
                        self.id = kwargs[key]
                    if key == 'size':
                        self.size = kwargs[key]
                    if key == 'x':
                        self.x = kwargs[key]
                    if key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

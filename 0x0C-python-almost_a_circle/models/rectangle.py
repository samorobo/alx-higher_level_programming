from base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        return self.width * self.height

    def display(self):
        for pos_y in range(self.__y):
            print()
        for row in range(self.__height):
            for pos_x in range(self.__x):
                print(' ', end='')
            for column in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        count = 1
        if args:
            for arg in args:
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.width = arg
                elif count == 3:
                    self.height == arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
                count +=1
        else:
            if kwargs:
                for key in kwargs:
                    if key == 'id':
                        self.id = kwargs[key]
                    if key == 'width':
                        self.width = kwargs[key]
                    if key == 'height':
                        self.height = kwargs[key]
                    if key == 'x':
                        self.x = kwargs[key]
                    if key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height, 'width': self.width}

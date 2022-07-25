#!/usr/bin/python3
class Rectangle:
    __width = None
    __height = None
    area = 0
    perimeter = 0
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ''
        self.print_symbol = str(self.print_symbol)
        if self.__height == 0 or self.width == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + self.print_symbol
            if i < (self.__height - 1):
                string = string + '\n'
        return string

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(
            eval(str(self.__width)), eval(str(self.__height))))

    def __del__(self):
        print("Bye rectangle...")
        self.number_of_instances -= 1

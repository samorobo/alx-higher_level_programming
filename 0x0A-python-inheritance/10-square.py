#!/usr/bin/python3
'''
BaseGeometry module
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' class Square '''
    def __init__(self, size):
        ''' Argument:
            @size: size of the square
        '''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

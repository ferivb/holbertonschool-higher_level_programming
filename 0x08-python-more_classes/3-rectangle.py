#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle: instantation
    * Private instance Attribute = height
    * Private instance Attribute = width"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private getter for Rectangle's width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """This sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Private getter for Rectangle's height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """This sets the value for width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Method to return Rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to return Rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Method to return Rectangle's graphical representation using '#'"""
        if self.__width == 0 or self.__height == 0:
            return("")
        else:
            row = self.__width * "#"
            drawing = row
            for i in range(self.__height - 1):
                drawing += "\n" + row
            return drawing

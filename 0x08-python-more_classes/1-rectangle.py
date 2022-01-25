#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle: instantation
    * Private instance Attribute = height
    * Private instance Attribute = width"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

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

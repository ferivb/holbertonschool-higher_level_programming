#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square with a private size"""

    def __init__(self, size=0):
        """Initializes the square with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of the Square Method"""
        return self.__size * self.__size

    @property
    def size(self):
        """Makes an attribute out of a method"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value provided in main as the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

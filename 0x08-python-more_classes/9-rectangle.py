#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle: takes width and height.
    Can be deleted, has a counter of instances"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor and instance counter"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

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
            row = self.__width * str(self.print_symbol)
            drawing = row
            for i in range(self.__height - 1):
                drawing += "\n" + row
            return drawing

    def __repr__(self) -> str:
        """Gives instructions to eval() on how to create the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destroys the instance, decreases instance counter and
        prints a message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2


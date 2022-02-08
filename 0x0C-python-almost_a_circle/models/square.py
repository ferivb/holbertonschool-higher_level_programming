#!/usr/bin/python3
"""Class Rectangle that inherits from Base"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Inherits from Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """[Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

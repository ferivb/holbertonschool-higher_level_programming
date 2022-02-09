#!/usr/bin/python3
"""This class will be the “base” of all other classes in this project"""
import json


class Base:
    """Manages id attribute in all future classes
    and to avoid duplicating the same code (by extension,
    same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

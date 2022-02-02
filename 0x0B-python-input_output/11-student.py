#!/usr/bin/python3
""" Class student with dictionary of itself"""


class Student:
    """Instance attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to create dictionary with filtered
        self's info"""
        new_list = {}
        if isinstance(attrs, list):
            for a in attrs:
                if a in self.__dict__:
                    new_list[a] = self.__dict__[a]
            return new_list
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of the Student instance"""
        for a in json:
            self.__dict__[a] = json[a]

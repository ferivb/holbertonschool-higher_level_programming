#!/usr/bin/python3
""" Class student with dictionary of itself"""


class Student:
    """Instance attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Method to create dictionary with self's info"""
    def to_json(self):
        return self.__dict__

#!/usr/bin/python3
"Takes a class and turns it into a JSON"


def class_to_json(obj):
    """ This __dict__ takes whatever object you
    pass it and turns it into a dictionary"""
    return obj.__dict__

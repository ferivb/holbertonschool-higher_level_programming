#!/usr/bin/python3
"JSON to Text File Function
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using a JSON representation"""
    with open(filename, 'w') as file:
        js = json.dump(my_obj, file)
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key is not None:
        a_dictionary.pop(key, -1)
    return a_dictionary

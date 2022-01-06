#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    update_list = {key: value}
    a_dictionary.update(update_list)
    return a_dictionary

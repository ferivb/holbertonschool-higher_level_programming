#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    k, v = a_dictionary.keys(), a_dictionary.values()
    for k in a_dictionary:
        new_dic[k] = a_dictionary[k] = v * 2
    return new_dic

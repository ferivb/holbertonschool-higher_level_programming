#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        i = len(my_list)

        while i >= 1:
            print("{:d}".format(i))
            i -= 1

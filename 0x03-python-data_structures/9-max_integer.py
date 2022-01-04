#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        n_list = []
        n_list = sorted(my_list, reverse=True)
        return(n_list[0])

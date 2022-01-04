#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) != 0):
        n_list = []
        n_list = sorted(my_list, reverse=True)
        return(n_list[0])
    else:
        return(None)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = tuple_a
    tb = tuple_b

    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    else:
        if (len(tuple_a) == 0):
            ta = (0, 0)
        if (len(tuple_b) == 0):
            tb = (0, 0)
        if (len(tuple_a) == 1):
            ta = (tuple_a[0], 0)
        if (len(tuple_b) == 1):
            tb = (tuple_b[0], 0)
        new_tuple = (ta[0] + tb[0], ta[1] + tb[1])
    return(new_tuple)

#!/usr/bin/env python3
def no_c(my_string):
    slist = list(my_string)
    for i in slist:
        if i == "c" or i == "C":
            slist.remove(i)
    return("".join(slist))

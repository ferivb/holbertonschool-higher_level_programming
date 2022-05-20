#!/usr/bin/python3
"""This module soport the find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of integers.
    list_of_integers: Unsorted int list."""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]

#!/usr/bin/python3
"""Append Fucntion"""


def append_write(filename="", text=""):
    """Appends text to the end of filename"""
    with open(filename, 'a', encoding='utf-8') as file:
        chars = file.write(text)
        return chars

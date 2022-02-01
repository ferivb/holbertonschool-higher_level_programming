#!/usr/bin/python3
"""Write/Overwrite Function"""


def write_file(filename="", text=""):
    """Overwrites the filename with the text
    returns number of chars writen"""
    with open(filename, 'w', encoding='utf-8') as file:
        chars = file.write(text)
        return chars

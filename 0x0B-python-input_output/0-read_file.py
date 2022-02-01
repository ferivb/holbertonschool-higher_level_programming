#!/usr/bin/python3
"""Read Function"""


def read_file(filename=""):
    """Reads the filename and prints it to the stdout"""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")

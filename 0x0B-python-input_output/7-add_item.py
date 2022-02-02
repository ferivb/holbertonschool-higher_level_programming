#!/usr/bin/python3
"""Script that takes arguments and turns
it into a list to the n save it in a file"""

import json
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
" Create the object or empty list "
try:
    object = load_from_json_file(filename)
except Exception:
    object = []

""" Fill in the list with the args """
for i in range(1, len(argv)):
    object.append(argv[i])

" Dump it on the file "
with open(filename, 'w') as file:
    json.dump(object, file)

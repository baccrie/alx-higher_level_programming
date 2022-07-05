#!/usr/bin/python3
"""
A json Script that incorporates
Modules from task 5 & 6
it uses function from module 5 to save
command line arguement to the list jsonList
and uses fumction from module 6 to print the list
"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


i = len(sys.argv)
jsonList = []
for a in range(1, i):
    jsonList.append(sys.argv[a])

save_to_json_file(jsonList, 'add_item.json')
load_from_json_file('add_item.json')

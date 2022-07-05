#!/usr/bin/python3
"""
"A JSON script coupled with command line arguement"""


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

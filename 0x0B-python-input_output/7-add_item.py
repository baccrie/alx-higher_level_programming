#!/usr/bin/python3
"""A magical module"""


import sys
import json
import os.path
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if os.path.exists("add_item.json"):
    pass
else:
    with open("add_item.json", 'w') as f:
        f.write("[]")

n = len(sys.argv)

obj = load_from_json_file("add_item.json")

for i in range(1, n):
    obj.append(sys.argv[i])


save_to_json_file(obj, "add_item.json")

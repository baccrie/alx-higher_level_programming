#!/usr/bin/python3
"""Copyright 2022 © baccrie"""

import json
import os
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_to_save = []
for i in sys.argv:
    list_to_save.append(i)
if len(list_to_save) >= 1:
    list_to_save.pop(0)

if os.path.exists('add_item.json'):
    data = load_from_json_file('add_item.json')
    for i in list_to_save:
        data.append(i)
    save_to_json_file(data, 'add_item.json')

else:
    save_to_json_file(list_to_save, 'add_item.json')

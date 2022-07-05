#!/usr/bin/python3
"""
A JSON SCRIPT WRITTEN BY baccrie
"""

import json


def load_from_json_file(filename):
    """
    A function that dumps from JSON to script
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        new = json.load(f)
        return (new)

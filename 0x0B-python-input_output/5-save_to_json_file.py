#!/usr/bin/python3
"""writes obj to a json file"""

import json


def save_to_json_file(my_obj, filename):
    """saves the text to a json file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)

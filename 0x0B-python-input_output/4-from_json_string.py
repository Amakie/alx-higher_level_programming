#!/usr/bin/python3
"""function for the python equivalent of a json object"""

import json


def from_json_string(my_str):
    """returns python represntation of a json string"""
    return (json.loads(my_str))

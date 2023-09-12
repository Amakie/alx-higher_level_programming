#!/usr/bin/python3
"""creates an object froma json file"""

import json


def load_from_json_file(filename):
    """obj represntation of a json file"""
    with open(filename) as f:
        return (json.load(f))

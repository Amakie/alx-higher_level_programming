#!/usr/bin/python3
"""functions that creates the json equivalent of an object"""


def to_json_string(my_obj):
    """returns the json represntation of the object"""

    return (json.dumps(my_obj))

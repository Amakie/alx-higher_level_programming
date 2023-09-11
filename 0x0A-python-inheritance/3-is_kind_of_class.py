#!/usr/bin/python3
"""module defines object as instance of a class"""


def is_kind_of_class(obj, a_class):
    """Defines class with attributes"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

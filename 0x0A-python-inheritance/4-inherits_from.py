#!/usr/bin/python3
"""defines an object using booleen values"""


def inherits_from(obj, a_class):
    """This functions defines the object"""

    if (issubclass(type(obj), a_class) and (type(obj) != a_class)):
        return True
    else:
        return False

#!/usr/bin/python3


"""This function adds two integers"""


def add_integer(a, b=98):
    """
    Args:
    a is an integer or float
    b is an integer or float

    Returns:
    sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError ("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError ("b must be an integer")
    return (int(a) + int(b))

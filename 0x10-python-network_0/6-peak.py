#!/usr/bin/python3
"""find peak  in a list of unsorted integers"""


def find_peak(list_of_integers):
    """sort the array and return the last element"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]

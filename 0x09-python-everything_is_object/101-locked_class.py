#!/usr/bin/python3
"""Defines a locked class called LockedClass"""


class LockedClass:
    """
    A class that does not allow any other instances
    Unless it called first name
    """
    __slot__ = [first_name]

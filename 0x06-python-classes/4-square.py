#!/usr/bin/python3

"""Defines a class called Square"""


class Square:

    """Initializes a private attribute called size"""
    def __init__(self, size=0):

        """defines the private attribute"""
        self.__size = size

    """defines a public instance method"""
    def area(self):

        """returns the current area"""
        return (self.__size ** 2)

    @property
    def size(self):
        """returns size"""

    @size.setter
    def size(self, value):
        """mutates the class to add value"""

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

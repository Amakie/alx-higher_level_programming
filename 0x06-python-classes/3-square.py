#!/usr/bin/python3

"""Defines a class called Square"""


class Square:

    """Initializes a private attribute called size"""
    def __init__(self, size=0):

        """defines the private attribute"""
        self.__size = size

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")

    """defines a public instance method"""
    def area(self):

        """returns the current area"""
        return (self.__size ** 2)

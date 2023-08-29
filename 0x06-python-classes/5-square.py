#!/usr/bin/python3

"""Defines a class called Square"""


class Square:

    """Initializes a private attribute called size"""
    def __init__(self, size=0):

        """defines the private attribute"""
        self.__size = size

    @property
    def size(self):
        """returns size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """mutates the class to add value"""

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

    """defines a public instance method"""
    def area(self):

        """returns the current area"""
        return (self.__size ** 2)

     def my_print(self):
        """prints in the square with char #"""

        if self.__size != 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

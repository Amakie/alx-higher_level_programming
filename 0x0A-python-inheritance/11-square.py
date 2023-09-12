#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Str method """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ Return the area of the square"""
        return self.__size * self.__size

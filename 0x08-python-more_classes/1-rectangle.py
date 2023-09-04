#!/usr/bin/python3

"""This module defines a class called rectangle"""


class Rectangle:
    """This is an empty class"""

    def __init__(self, width=0, height=0):
        """This initializes the rectangle class
        The class has two attributes. Width and height
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """Defines the width attribute"""
            return self._width

        @width.setter
        def width(self, value):
            """sets the value for width"""
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Defines the height attribute"""
            return self_height

        @height.setter
        def height(self, value):
            """sets the value for width"""
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value

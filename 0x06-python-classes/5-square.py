#!/usr/bin/python3

"""This class defines a square."""


class Square:
    """Initializes a private attribute called size"""

    def __init__(self, size=0):
        """defines the private attribute"""

        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of square

        Returns:
            int: an integer value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """defines the size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #"""

        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

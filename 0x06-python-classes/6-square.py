#!/usr/bin/python3

"""This class defines a square."""


class Square:
    """defines the private attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """defines the private attribute"""

        self.__size = 0
        self.__position = (0, 0)
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns a tuple of 2 positive integers representing the position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""

        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns size"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square with the #"""

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

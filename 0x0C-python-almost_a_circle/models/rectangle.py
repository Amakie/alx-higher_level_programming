#!/usr/bin/python3
"""module that inherits from the base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__ = id

"""returns values for various attributes"""
@property
def width(self):
    return (self.__width)

def height(self):
    return (self.__height)

def x(self):
    return (self.__x)

def y(self):
    return (self.__y)

@width.setter
def width(self, value):
    if type(value) != int:
        raise TypeError("width must be an integer")
    if type(value) <= 0:
        raise ValueError("width must be > 0")
    self.__width = width
    
@height.setter
def height(self, value):
    if type(value) != int:
        raise TypeError("height must be an integer")
    if type(value) <= 0:
        raise ValueError("height must be > 0")
    self.__height = height

@x.setter
def x(self, value):
    if type(value) != int:
        raise TypeError("x must be an integer")
    if type(value) <= 0:
        raise ValueError("x must be > 0")
    self.__x = x

@y.setter
def y(self, value):
    if type(value) != int:
        raise TypeError("y must be an integer")
    if type(value) <= 0:
        raise ValueError("y must be > 0")
    self.__y = y


    """initiates a public method that returns the area of the rectangle"""
    def area(self):
        rec_area = self.__width * self.__height
        return rec_area

    """prints a rectangle display using hashtags"""
    def display(self):
        if self.__width == 0 or self.__height == 0:
            print("")
            return
        
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    """string representation of the rectangle"""
    def __str__(self):
        return f"[rectangle] ({self.id}) {self.__x}/{self.__y} - \ {self.__width}/{self.__height}"
    
    """update class with public method"""
    def update(self, *args):
        pass
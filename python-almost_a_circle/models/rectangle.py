#!/usr/bin/python3
"""First Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        self.__width = width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        self.__height = height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        self.__x = x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        self.__y = y

    @y.setter
    def y(self, value):
        self.__y = value

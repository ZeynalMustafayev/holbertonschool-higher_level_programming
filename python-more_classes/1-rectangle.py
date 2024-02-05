#!/usr/bin/python3
"""Define a class Square."""


class Rectangle:
    """Square class with private attribute size"""
    def __init__(self, width=0, height=0):
        """Initialize Square with size attribute"""
        self.width = width
        self.height = height

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                TypeError("width must be an integer")
            elif value < 0:
                ValueError("width must be >= 0")
            else:
                self.__height = value

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                TypeError("height must be an integer")
            elif value < 0:
                ValueError("height must be >= 0")
            else:
                self.__width = value

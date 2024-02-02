#!/usr/bin/python3
"""Define a class Square."""

class Square:
    def __init__(self, size=0):
        """Square class with private attribute size"""
        self.__size = size

    @property
    def size(self):
        self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            TypeError("size must be an integer")
        elif value < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the
        current square area."""
        return self.__size**2

    def my_print(self):
        """Public instance method that returns the
        current square area."""
        for _ in range(self.__size):
            print("#" * self.__size)

#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method that returns the
        current square area."""
        return (self.__size**2)

    def __eq__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size == __value.size

    def __ne__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size != __value.size

    def __lt__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size < __value.size

    def __le__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size <= __value.size

    def __gt__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size > __value.size

    def __ge__(self, __value):
        if not isinstance(__value, (Square)):
            raise TypeError("value must be a Square")
        return self.size >= __value.size

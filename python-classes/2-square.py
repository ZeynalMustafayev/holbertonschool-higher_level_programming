#!/usr/bin/python3
class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0):
        """Initialize Square with size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

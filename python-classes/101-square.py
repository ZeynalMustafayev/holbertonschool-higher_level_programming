#!/usr/bin/python3
"""Square"""


class Square:
    """class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """Prints area using # sign"""
        res = ""
        if self.__size == 0:
            res += "\n"
        else:
            for i in range(self.position[1]):
                res += "\n"

            for i in range(self.size):
                for j in range(self.position[0]):
                    res += " "
                for j in range(self.__size):
                    res += "#"
                res += "\n"
        return res[:-1]

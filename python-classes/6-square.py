#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square class with private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """Square class with private attribute size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area."""
        return self.__size**2

    def my_print(self):
        """Public instance method that prints the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

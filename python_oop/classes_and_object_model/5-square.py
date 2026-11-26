#!/usr/bin/env python3
"""Defines a Square class that can print itself with '#'."""


class Square:
    """Represents a square with a private, validated size."""

    def __init__(self, size=0):
        """Initializes a square, validating its size through the setter."""
        self.size = size

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square, validating its value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)

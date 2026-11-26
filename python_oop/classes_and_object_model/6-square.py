#!/usr/bin/env python3
"""Defines a Square class that prints with '#' and has a position."""

class Square:
    """Represents a square with a validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square, validating size and position via setters."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square, validating its value."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Returns the square drawn with '#' and offset by its position."""
        if self.__size == 0:
            return ""
        x, y = self.__position
        rows = [" " * x + "#" * self.__size] * self.__size
        return "\n" * y + "\n".join(rows)

    def my_print(self):
        """Prints the square using the '#' character."""
        print(str(self))

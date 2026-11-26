#!/usr/bin/env python3
"""Defines a Square class with a validated private size attribute."""


class Square:
    """Represents a square with a private, validated size."""

    def __init__(self, size=0):
        """Initializes a square, validating its size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

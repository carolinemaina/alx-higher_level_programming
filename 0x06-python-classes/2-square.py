#!/usr/bin/python3
"""Define a Square class"""


class Square:
    """Represent the square"""

    def __init__(self, size=0):
        """Initialize new Square
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

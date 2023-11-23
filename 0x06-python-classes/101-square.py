#!/usr/bin/python3
"""Define square class"""


class Square:
    """Represent the square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square
        Args:
            size (int): size of new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set current size of square"""
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
        """Get/set postion parameters"""
        return self.__position

    @position.setter
    def position(self, value):
        """Get/set postion value parameters"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Get/set area of square"""
        return self.size ** 2

    def my_print(self):
        """Get/set print parameters"""
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

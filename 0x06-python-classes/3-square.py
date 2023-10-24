#!/usr/bin/python3

"""
This module contains a definition for a Square class.
"""


class Square:
    """
    This class represents a square geometric shape.

    Attributes:
        __size (int): The size of the square. It is a private attribute.
    """

    def __init__(self, size=0):
        """
        The constructor for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

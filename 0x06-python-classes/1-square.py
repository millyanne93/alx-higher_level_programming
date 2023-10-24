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

    def __init__(self, size):
        """
        The constructor for the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

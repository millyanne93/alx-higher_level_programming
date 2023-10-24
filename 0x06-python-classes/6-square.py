#!/usr/bin/python3

"""
This module contains a definition for a Square class.
"""


class Square:
    """
    This class represents a square geometric shape.

    Attributes:
        __size (int): The size of the square. It is a private attribute.
        __position (tuple): The position of the square in 2D space.
                            It is a private attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor for the Square class.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square.
                                        Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is not
                       a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter for position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position attribute.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character # at its position.

        Prints an empty line if size is equal to 0.

        Uses spaces for horizontal positioning and newline characters
        for vertical positioning.

        Don't fill lines by spaces when position[1] > 0.
        """

        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size
                            for _ in range(self.__size)))

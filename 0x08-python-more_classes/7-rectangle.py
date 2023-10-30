#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol: Used as a symbol for string
        representation. Can be any type.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the character(s)
        stored in print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = '\n'.join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])
        return rect

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

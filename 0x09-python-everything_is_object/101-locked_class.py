#!/usr/bin/python3

"""Defines a locked class with limited attribute access."""


class LockedClass:
    """Restricts new attributes to 'first_name' only."""

    __slots__ = ["first_name"]

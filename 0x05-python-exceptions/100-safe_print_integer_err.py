#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    Safely prints an integer to the standard output and handles errors.
    
    Args:
        value: The value to be printed.

    Returns:
        True if the value is successfully printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)

#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase."""
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print(result)

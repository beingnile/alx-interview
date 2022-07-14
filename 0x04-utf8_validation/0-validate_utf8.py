#!/usr/bin/env python3
"""Defines a function that checks if a data set represents
a valid UTF-8 encoding
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding

    Args:
        Data: The data set

    Returns:
        True if data is a valid UTF-8 encoding, else False
    """
    for val in data:
        try:
            (val).to_bytes((val.bit_length() + 7) // 8, 'big').decode('utf-8')
        except UnicodeError:
            return False
    return True

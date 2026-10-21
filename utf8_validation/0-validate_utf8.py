#!/usr/bin/python3
"""Validate UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is a valid UTF-8 encoding."""
    bytes_to_check = 0

    for num in data:
        byte = num & 0xFF

        if bytes_to_check == 0:
            if byte >> 7 == 0:
                continue
            elif byte >> 5 == 0b110:
                bytes_to_check = 1
            elif byte >> 4 == 0b1110:
                bytes_to_check = 2
            elif byte >> 3 == 0b11110:
                bytes_to_check = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0

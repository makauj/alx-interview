#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """Check if a given data set is valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing byte values.

    Returns:
        bool: True if the data is valid UTF-8, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Check the number of leading
        # 1s in the binary representation of the byte
        byte = byte & 0xFF
        
        if num_bytes == 0:
            mask = 0x80
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if the byte is a continuation byte
            if not (byte & 0xC0 == 0x80):
                return False
        num_bytes -= 1
    return num_bytes == 0

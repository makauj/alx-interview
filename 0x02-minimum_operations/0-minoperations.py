#!/usr/bin/python3
"""Minimum operations"""


def minOpereations(n):
    """
    Script that only does two commands: copy all and paste all
    args:
        n: an integer. If n cannot be acheived, return 0
    Return:
        the minimum number of operations needed to get n H characters
        0 if n is not possible
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations

#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Function that returns a list of integers"""
    triangle = [] # initialize an empty triangle

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] * (i + 1) # start each row with 1
        for j in range(1, i):
            # Fill in the inner values
            row[j] = triangle[i - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

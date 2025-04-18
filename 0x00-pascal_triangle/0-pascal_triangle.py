#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle
    of n.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        list: A list of lists of integers representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start a new row with 1
        row = [1]
        if triangle:
            last_row = triangle[-1]
            # Build the middle values of the row
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # End the row with 1
        triangle.append(row)

    return triangle

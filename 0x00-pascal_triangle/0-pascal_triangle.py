#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
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

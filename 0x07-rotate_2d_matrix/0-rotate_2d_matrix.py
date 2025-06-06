#!/usr/bin/python3
"""Python script to rotate a 2D matrix clockwise by 90 degrees."""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix clockwise by 90 degrees."""
    if not matrix or not matrix[0]:
        return
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

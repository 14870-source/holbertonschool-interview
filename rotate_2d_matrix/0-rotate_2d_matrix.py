#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """Rotate the matrix in-place."""
    n = len(matrix)

    # Transpose the matrix
    for row in range(n):
        for col in range(row + 1, n):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row], matrix[row][col]
            )

    # Reverse each row
    for row in matrix:
        row.reverse()

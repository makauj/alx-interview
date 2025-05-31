#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""
import sys


def generate_solutions(row, column):
    """Generate solutions for the N queens problem."""
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    """Place a queen on the board."""
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    """Check if position is safe"""
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """initialize the program."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():
    """Generate and run solutions for the N queens problem."""
    n = init()
    solutions = generate_solutions(n, n)
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()

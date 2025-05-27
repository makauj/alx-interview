#!/usr/bin/python3
"""
A program that solves the N queens problem.
The N queens puzzle is the problem of placing N chess queens on an N×N
chessboard so that no two queens threaten each other.
"""
import sys


def print_usage_and_exit():
    """Print usage message and exit."""
    print("Usage: nqueens N")
    sys.exit(1)


def generate_solutions(n, row=0, board=None, solutions=None):
    """Generate all solutions for the N queens problem."""
    if board is None:
        board = [-1] * n
    if solutions is None:
        solutions = []

    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            generate_solutions(n, row + 1, board, solutions)
            board[row] = -1  # backtrack

    return solutions


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def n_queens():
    """Main entry point for the N queens problem solver."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = generate_solutions(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])


if __name__ == "__main__":
    n_queens()

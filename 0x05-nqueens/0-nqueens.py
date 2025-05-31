#!/usr/bin/python3
"""
A program that solves the N queens problem.
"""
import sys


def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r, c in enumerate(solution):
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve_n_queens(n, row=0, solution=[], solutions=[]):
    """Recursively solve the N queens problem."""
    if row == n:
        solutions.append([[r, c] for r, c in enumerate(solution)])
        return

    for col in range(n):
        if is_safe(solution, row, col):
            solve_n_queens(n, row + 1, solution + [col], solutions)


def main(n):
    """Main function to run the N queens solver."""
    if n < 4:
        print("N must be at least 4")
        return
    solutions = []
    solve_n_queens(n, 0, [], solutions)
    for sol in solutions:
        print(sol)
    print(f"Total solutions for {n}-queens: {len(solutions)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-nqueens.py N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    main(n)

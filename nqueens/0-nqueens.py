#!/usr/bin/python3
"""Solve the N Queens problem using backtracking."""
import sys


def solve_nqueens(n):
    """Find and print all solutions to the N Queens problem."""
    solution = []
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()

    def backtrack(row):
        if row == n:
            print(solution)
            return

        for col in range(n):
            positive = row + col
            negative = row - col

            if (col in columns or
                    positive in positive_diagonals or
                    negative in negative_diagonals):
                continue

            solution.append([row, col])
            columns.add(col)
            positive_diagonals.add(positive)
            negative_diagonals.add(negative)

            backtrack(row + 1)

            solution.pop()
            columns.remove(col)
            positive_diagonals.remove(positive)
            negative_diagonals.remove(negative)

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)

#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    # Check the current column on this row
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True


def solve_n_queens_util(board, row, n):
    if row == n:
        print_solution(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            res = solve_n_queens_util(board, row + 1, n) or res
            board[row] = -1

    return res


def solve_n_queens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_n_queens_util(board, 0, n)


def print_solution(board):
    n = len(board)
    solution = [[i, board[i]] for i in range(n)]
    print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)

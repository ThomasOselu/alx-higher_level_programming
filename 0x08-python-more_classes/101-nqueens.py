#!/usr/bin/python3
"""Placing N non-attacking queens on an NxN chessboard"""
import sys


matrix = []
board = []


def result():
    """Prints result."""
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                matrix[row][1] = col
    return matrix


def backtrack(r, n, col, posDiag, negDiag):
    """recursive function and backtracks
    args:
      r: row 0, our starting point
      n: our N chessboard
      col:our column set
      pos_dia: positive diagonal
      neg_dia: negative diagonal
    """
    global board
    if r == n:
        print(result())
        return

    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)

        board[r][c] = 1

        backtrack(r + 1, n, col, posDiag, negDiag)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)

        board[r][c] = 0


def solve_n_queens(n):
    """ Solve N Queens. """
    col = set()
    posDiag = set()
    negDiag = set()

    global matrix
    global board
    matrix = [[c + r for c in range(2)] for r in range(n)]
    board = [[0 for i in range(n)] for i in range(n)]

    backtrack(0, n, col, posDiag, negDiag)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

num = sys.argv[1]

try:
    num_int = int(num)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if num_int < 4:
    print("N must be at least 4")
    sys.exit(1)

solve_n_queens(num_int)

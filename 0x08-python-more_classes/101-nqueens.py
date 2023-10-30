#!/usr/bin/python3
import sys


def init_board(n):
    """
    Initialize an `n`x`n` sized chessboard with 0's.
    Args:
        n (int): The size of the chessboard.
    Returns:
        list: An `n`x`n` sized chessboard initialized with 0's.
    """
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return board


def board_deepcopy(board):
    """
    Return a deepcopy of a chessboard.
    Args:
        board (list): The chessboard to be copied.
    Returns:
        list: A deepcopy of the input chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """
    Return the list of lists representation of a solved chessboard.
    Args:
        board (list): The chessboard to be solved.
    Returns:
        list: A list of lists representing the solved chessboard.
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(board, row, col):
    """
    X out all invalid spots on the chessboard
    from a given position.
    Args:
        board (list): The chessboard to be updated.
        row (int): The row index of the position.
        col (int): The column index of the position.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solve the N-Queens problem by placing
    queens on the chessboard and checking solutions.
    Args:
        board (list): The chessboard to be solved.
        row (int): The current row index.
        queens (int): The current number of queens placed on the chessboard.
        solutions (list): The current list of solutions found.
    Returns:
        list: An updated list of solutions found
        after placing queens on the current row.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)

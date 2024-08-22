# backtracker.py
from Sudoku_solver.Sudoku_base import SudokuBase

class backtracker(SudokuBase):
    def __init__(self, board=None):
        self.board = board if board is not None else self.get_board()
    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None
    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i
                self.print_board()

                if self.solve():
                    return True
                self.board[row][col] = 0
        return False
# my_algm.py
from Sudoku_solver.Sudoku_base import SudokuBase

class my_algm(SudokuBase):
    def is_valid(self, num, row, col):
        # Check if 'num' can be placed at board[row][col]
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == num:
                    return False
        return True
    def find_valid_spots(self, num):
        valid_spots = []
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0 and self.is_valid(num, row, col):
                    valid_spots.append((row, col))
        return valid_spots
    def place_number(self, num):
        valid_spots = self.find_valid_spots(num)
        subgrid_valid_spots = {}

        for spot in valid_spots:
            row, col = spot
            subgrid = (row // 3, col // 3)
            if subgrid not in subgrid_valid_spots:
                subgrid_valid_spots[subgrid] = []
            subgrid_valid_spots[subgrid].append(spot)

        # Direct placement if only one valid spot in any subgrid
        for spots in subgrid_valid_spots.values():
            if len(spots) == 1:
                return spots[0]

        return None
    def solve(self):
        return self.solve_recursive()

    def solve_recursive(self):
        # Select the number with the highest frequency
        number_count = [0] * 10
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    number_count[self.board[row][col]] += 1

        for num in range(1, 10):
            if number_count[num] > 0:
                spot = self.place_number(num)
                if spot:
                    row, col = spot
                    self.board[row][col] = num
                    if self.solve_recursive():
                        return True
                    self.board[row][col] = 0

        # Try classic backtracking if no direct placement found
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, row, col):
                            self.board[row][col] = num
                            if self.solve_recursive():
                                return True
                            self.board[row][col] = 0
                    return False
        return True
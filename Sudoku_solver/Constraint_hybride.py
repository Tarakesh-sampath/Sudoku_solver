# ConstraintHybride.py
from Sudoku_solver.Sudoku_base import SudokuBase

class Algm_1(SudokuBase):
    #A hybride of Constraint Propagation(find the feasable possibility and reduce the backtracking branch) and Backtracking
    """This algorithm can be described as a constraint satisfaction-based backtracking hybrid. The use of constraint propagation 
    helps limit the number of possibilities the backtracking algorithm has to explore, making the overall approach more efficient 
    than simple brute-force backtracking."""

    def __init__(self, board=None):
        self.board = board if board is not None else None
        self.iterations = 0 
    def find_valid_spots(self):
        invalid_spots = set()
        for num in range(1, 10):
            for i in range(9):
                for j in range(9):
                    if self.board[i][j] == num:
                        # Mark the entire row and column as invalid
                        invalid_spots.update((i, x) for x in range(9))
                        invalid_spots.update((x, j) for x in range(9))
                        # Mark the entire 3x3 box as invalid
                        invalid_spots.update((((i // 3)*3)+ x,((j//3)*3)+ y) for x in range(3) for y in range(3))
        return invalid_spots
    def get_possible_values(self, i, j):
        used_numbers = set()

        # Check row and column
        for k in range(9):
            used_numbers.add(self.board[i][k])
            used_numbers.add(self.board[k][j])

        # Check 3x3 box
        for x in range(3):
            for y in range(3):
                used_numbers.add(self.board[((i // 3)*3) + x][((j//3)*3)+ y])
        return {num for num in range(1, 10) if num not in used_numbers}
    def solve(self):
        self.iterations += 1
        # Find the first empty spot
        min_possible_values = 10
        min_spot = None
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    possible_values = self.get_possible_values(i, j)
                    if len(possible_values) < min_possible_values:
                        min_possible_values = len(possible_values)
                        min_spot = (i, j)

        if not min_spot:
            return True  # No empty spots left, board is solved
        i, j = min_spot
        possible_values = self.get_possible_values(i, j)
        for num in possible_values:
            self.board[i][j] = num
            self.print_board(f"Placed {num} at ({i}, {j})")
            if self.solve():
                return True
            self.board[i][j] = 0
            self.print_board(f"Removed {num} from ({i}, {j})")
        return False
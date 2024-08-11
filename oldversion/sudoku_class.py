from sudoku_base import SudokuBase
from collections import defaultdict
import copy

class Backtracker(SudokuBase):
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
                print("\n")

                if self.solve():
                    return True
                self.board[row][col] = 0
        return False

class Algm_1(SudokuBase):
    #A hybride of Constraint Propagation(find the feasable possibility and reduce the backtracking branch) and Backtracking
    """This algorithm can be described as a constraint satisfaction-based backtracking hybrid. The use of constraint propagation 
    helps limit the number of possibilities the backtracking algorithm has to explore, making the overall approach more efficient 
    than simple brute-force backtracking."""

    def __init__(self, board=None):
        self.board = board if board is not None else None
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

if __name__ == "__main__":
    
    #default board for all model
    #classes

    def make_work(ch):
        if ch==1:
            #classic backtracking
            m1= Backtracker(copy.deepcopy(SudokuBase.board))
            m1.print_board("Initial Board:")
            m1.solve()
            input("Press Enter to continue...")
        if ch==2:
            #A hybride of Constraint Propagation(find the feasable possibility and reduce the backtracking branch) and Backtracking
            m2 = Algm_1(copy.deepcopy(SudokuBase.board))
            m2.print_board("Initial Board:")
            m2.solve()
            input("Press Enter to continue...")
        if ch==3:
            m3 = my_algm(copy.deepcopy(SudokuBase.board))
            m3.print_board("Initial Board:")
            input("Press Enter to continue...")
            if m3.solve():
                print("Solution found:")   
                m3.print_board("Final board")
            else:
                print("No solution exists.")
        if ch>=4:
            exit()
    while(True):
        make_work(int(input("""Enter the algorithum to run 
          1 - classic backtracking 
          2 - Constraint Propagation and Backtracking 
          3 - my algorithm
          4 - exit
        input:""")))
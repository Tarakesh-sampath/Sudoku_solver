import os
class SudokuBase:
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    def __init__(self, board=None):
        self.board = board if board is not None else None
    def get_board(self):
        board = []
        print("Enter the Sudoku puzzle row by row (use 0 for empty cells):")
        for _ in range(9):
            while True:
                row = input()
                try:
                    row = [int(x) for x in row.split()]
                    if len(row) == 9:
                        board.append(row)
                        break
                    else:
                        print("Please enter exactly 9 numbers.")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
        return board
    def print_board(self, text=""):
        size = len(self.board)
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen based on the OS
        print("\n", text)
        print("+---------+---------+---------+")
        for i in range(size):
            if (i) % 3 == 0 and i != 0:
                print("+---------+---------+---------+")
            row = "| "
            for j in range(size):
                row += (str(self.board[i][j]) if self.board[i][j] != 0 else " ")
                if (j + 1) % 3 == 0 and j != 0:
                    row += " | "
                else:
                    row += "  "
            print(row)
            if i == size - 1:
                print("+---------+---------+---------+")
    def is_valid(self, num, pos):
        # Check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False
        return True
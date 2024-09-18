# main.py
from Sudoku_solver.Backtracker import backtracker
from Sudoku_solver.Constraint_hybride import ConstraintHybride
from Sudoku_solver.My_Algm import my_algm
from Sudoku_solver.Sudoku_base import SudokuBase
import copy
import os
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input("""
        Enter the algorithm to run:
        1 - Classic Backtracking
        2 - Constraint Propagation and Backtracking
        3 - My Algorithm
        4 - Exit
        Input: """))

        if choice == 1:
            #classic backtracking
            solver = backtracker(copy.deepcopy(SudokuBase.board))
        elif choice == 2:
            #A hybride of Constraint Propagation(find the feasable possibility and reduce the backtracking branch) and Backtracking
            solver = ConstraintHybride(copy.deepcopy(SudokuBase.board))
        elif choice == 3:
            solver = my_algm(copy.deepcopy(SudokuBase.board))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        solver.print_board("Initial Board:")
        input("Press Enter to continue...")
        if solver.solve():
            solver.print_board("Final Board:")
        else:
            print("No solution exists.")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()

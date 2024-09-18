import time
import tracemalloc
import copy
import os
from Sudoku_solver.Backtracker import backtracker
from Sudoku_solver.Constraint_hybride import Algm_1
from Sudoku_solver.My_Algm import my_algm
from Sudoku_solver.Sudoku_base import SudokuBase

def run_algorithm(algorithm_class):
    # Start memory tracking
    tracemalloc.start()
    
    # Create a copy of the default board
    board = copy.deepcopy(SudokuBase.board)
    solver = algorithm_class(board)
    
    # Start timing
    start_time = time.time()
    
    # Solve the puzzle
    solver.iterations = 0  # Reset iterations for the solver
    solved = solver.solve()
    
    # Stop timing
    end_time = time.time()
    
    # Get current memory usage
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Calculate metrics
    execution_time = end_time - start_time
    memory_used = peak / 10**6  # Convert to MB
    
    return {
        'Algorithm': solver.__class__.__name__,
        'Execution Time (s)': execution_time,
        'Iterations': solver.iterations,
        'Memory Used (MB)': memory_used,
        'Solved': solved
    }

def display_metrics(metrics):
    print("\nMetrics:")
    print("+--------------------------------+-----------------------+-------------------+-----------------------+-----------+")
    print("| Algorithm                      | Execution Time (s)    | Iterations        | Memory Used (MB)      | Solved    |")
    print("+--------------------------------+-----------------------+-------------------+-----------------------+-----------+")
    for metric in metrics:
        print(f"| {metric['Algorithm']:30} | {metric['Execution Time (s)']:21.5f} | {metric['Iterations']:17} | {metric['Memory Used (MB)']:21.5f} | {metric['Solved']}      |")
        print("+--------------------------------+-----------------------+-------------------+-----------------------+-----------+")

def main():
    algorithms = [backtracker, Algm_1, my_algm]
    metrics = []

    for algorithm in algorithms:
        metric = run_algorithm(algorithm)
        metrics.append(metric)
    os.system('cls' if os.name == 'nt' else 'clear')
    display_metrics(metrics)

if __name__ == "__main__":
    main()

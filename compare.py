import time
import tracemalloc
import cProfile
import pstats
import io
from Sudoku_solver.Backtracker import backtracker
from Sudoku_solver.Constraint_hybride import Algm_1
from Sudoku_solver.My_Algm import my_algm

# Multiple Sudoku puzzles for testing
sample_sudokus = [
    # Easy puzzle
    [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],
    # Medium puzzle
    [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ],
    # Hard puzzle
    [
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [4, 9, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 7, 6, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 3, 0],
        [0, 0, 0, 4, 1, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 2, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]

# Modify the measure_performance function to take multiple boards
def measure_performance(algorithm_class, algorithm_name, sample_sudokus):
    for idx, sudoku in enumerate(sample_sudokus):
        print(f"\nEvaluating {algorithm_name} on Sudoku puzzle {idx + 1}...")

        # Initialize the algorithm with the specific Sudoku board
        solver = algorithm_class(board=sudoku)

        # Measure time
        start_time = time.time()

        # Measure memory usage
        tracemalloc.start()
        solver.solve()
        memory_usage = tracemalloc.get_traced_memory()[1]  # Peak memory usage
        tracemalloc.stop()

        end_time = time.time()
        time_taken = end_time - start_time

        print(f"Time taken by {algorithm_name}: {time_taken:.4f} seconds")
        print(f"Memory used by {algorithm_name}: {memory_usage / 1024:.2f} KB")

# Function to profile branches and function calls
def profile_algorithm(algorithm_class, algorithm_name):
    print(f"\nProfiling {algorithm_name}...")
    
    solver = algorithm_class()

    pr = cProfile.Profile()
    pr.enable()

    # Run the algorithm
    solver.solve()

    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats()

    print(s.getvalue())

# Example comparison
algorithms = [
    (backtracker, "Backtracking Algorithm"),
    (my_algm, "Custom Algorithm"),
    (Algm_1, "Constraint Hybrid Algorithm")
]

for alg_class, alg_name in algorithms:
    measure_performance(alg_class, alg_name, sample_sudokus)
    profile_algorithm(alg_class, alg_name)

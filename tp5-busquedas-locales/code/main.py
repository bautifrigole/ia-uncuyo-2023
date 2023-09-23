from n_queens_solver import *

n_values = [4, 8, 10]
max_evaluations = 100000

for n in n_values:
    print(f"Solving {n}-Queens:")
    solver = HillClimbingSolver(n, max_evaluations)
    #solver = SimulatedAnnealingSolver(n, max_evaluations, 100.0, 0.95)
    #solver = GeneticAlgorithmSolver(n, 100, 1000, 0.1)
    board, attacks, evaluations = solver.solve()

    if attacks == 0:
        print(f"Solution found in {evaluations} evaluations:")
        print(board.board)
        board.plot()
    else:
        print(f"No solution found within {max_evaluations} evaluations.")
    print("\n")

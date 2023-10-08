import random
import math
from n_queens_board import NQueensBoard

class NQueensSolver:
    def __init__(self, n, max_evaluations):
        self.n = n
        self.max_evaluations = max_evaluations
        self.h_values = []

    def solve(self):
        current_board = NQueensBoard(self.n)
        current_attacks = current_board.calculate_attack_pairs()
        self.h_values.append(current_attacks)
        evaluations = 1

        while current_attacks > 0 and evaluations < self.max_evaluations:
            neighbor_board = NQueensBoard(self.n)
            row, col = random.sample(range(self.n), 2)
            neighbor_board.move_queen(row, current_board.board[col])
            neighbor_attacks = neighbor_board.calculate_attack_pairs()

            if self.is_neighboring_solution_better(neighbor_attacks, current_attacks):
                current_board = neighbor_board
                current_attacks = neighbor_attacks

            self.update_state()
            evaluations += 1
            self.h_values.append(current_attacks)

        return current_board, current_attacks, evaluations
    
    def is_neighboring_solution_better(self, neighbor_attacks: int, current_attacks: int):
        pass

    def update_state(self):
        pass

class NQueensBacktrackingSolver(NQueensSolver):
    def is_neighboring_solution_better(self, neighbor_attacks, current_attacks):
        return neighbor_attacks < current_attacks

    def solve(self):
        current_board = NQueensBoard(self.n)
        current_attacks = current_board.calculate_attack_pairs()
        self.h_values.append(current_attacks)
        evaluations = 1

        def backtrack(row):
            nonlocal current_attacks, current_board, evaluations

            if row == self.n:
                return True  # Se encontró una solución

            for col in range(self.n):
                if current_board.board[col] == -1:
                    current_board.board[col] = row
                    current_attacks = current_board.calculate_attack_pairs()
                    self.h_values.append(current_attacks)
                    evaluations += 1

                    if current_attacks == 0 or (evaluations >= self.max_evaluations):
                        return True

                    if backtrack(row + 1):
                        return True

                    # Si no se encontró una solución, deshacer el movimiento
                    current_board.board[col] = -1
                    self.h_values.append(current_board.calculate_attack_pairs())

            return False  # No se encontró solución en esta rama

        backtrack(0)
        current_board.plot()
        return current_board, current_attacks, evaluations


class NQueensForwardCheckingSolver(NQueensSolver):
    def is_neighboring_solution_better(self, neighbor_attacks, current_attacks):
        return neighbor_attacks < current_attacks

    def solve(self):
        current_board = NQueensBoard(self.n)
        current_attacks = current_board.calculate_attack_pairs()
        self.h_values.append(current_attacks)
        evaluations = 1

        def forward_check(row):
            nonlocal current_attacks, current_board, evaluations

            if row == self.n:
                return True  # Se encontró una solución

            for col in range(self.n):
                if current_board.board[col] == -1:
                    current_board.board[col] = row
                    forward_check(current_board, row, col)
                    current_attacks = current_board.calculate_attack_pairs()
                    self.h_values.append(current_attacks)
                    evaluations += 1

                    if current_attacks == 0 or (evaluations >= self.max_evaluations):
                        return True

                    if forward_check(row + 1):
                        return True

                    # Si no se encontró una solución, deshacer el movimiento
                    current_board.board[col] = -1
                    self.h_values.append(current_board.calculate_attack_pairs())

            return False  # No se encontró solución en esta rama

        forward_check(0)
        current_board.plot()
        return current_board, current_attacks, evaluations

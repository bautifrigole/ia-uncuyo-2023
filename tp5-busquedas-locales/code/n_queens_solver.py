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

class HillClimbingSolver(NQueensSolver):
    def is_neighboring_solution_better(self, neighbor_attacks: int, current_attacks: int):
        return neighbor_attacks < current_attacks

class SimulatedAnnealingSolver(NQueensSolver):
    def __init__(self, n, max_evaluations, initial_temperature, cooling_rate):
        self.n = n
        self.max_evaluations = max_evaluations
        self.temperature = initial_temperature
        self.cooling_rate = cooling_rate
        self.h_values = []
    
    def is_neighboring_solution_better(self, neighbor_attacks: int, current_attacks: int):
        delta_attacks = neighbor_attacks - current_attacks
        return delta_attacks <= 0 or random.random() < math.exp(-delta_attacks / self.temperature)
    
    def update_state(self):
        self.temperature *= self.cooling_rate

class GeneticAlgorithmSolver:
    def __init__(self, n, population_size, generations, mutation_rate):
        self.n = n
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = []
        self.h_values = []
    
    def solve(self):
        # Resuelve el problema utilizando el algoritmo genético
        self.initialize_population()
        for generation in range(self.generations):
            best_board = min(self.population, key=self.calculate_fitness)
            self.h_values.append(best_board.calculate_attack_pairs())
            if self.calculate_fitness(best_board) == 0:
                return best_board, 0, generation
            self.evolve()
        
        best_board = min(self.population, key=self.calculate_fitness)
        attacks = best_board.calculate_attack_pairs()
        
        return best_board, attacks, self.generations

    def initialize_population(self):
        # Generar una población inicial de soluciones aleatorias
        for _ in range(self.population_size):
            board = NQueensBoard(self.n)
            self.population.append(board)

    def calculate_fitness(self, board):
        # Calcular el valor de aptitud para un tablero dado
        return board.calculate_attack_pairs()

    def select_parents(self):
        # Seleccionar dos padres de la población actual utilizando torneos
        parents = []

        for _ in range(2):  # Seleccionar dos padres
            tournament_candidates = random.sample(self.population, 4)
            best_parent = min(tournament_candidates, key=self.calculate_fitness)
            parents.append(best_parent)

        return parents

    def crossover(self, parent1, parent2):
        # Realizar el cruce (crossover) para generar un nuevo tablero
        child = NQueensBoard(self.n)
        crossover_point = random.randint(1, self.n - 1)
        child.board = parent1.board[:crossover_point] + parent2.board[crossover_point:]
        return child

    def mutate(self, board):
        # Aplicar mutación a un individuo
        if random.random() < self.mutation_rate:
            index_to_mutate = random.randint(0, self.n - 1)
            new_value = random.randint(0, self.n - 1)
            board.move_queen(index_to_mutate, new_value)

    def evolve(self):
        # Algoritmo principal de evolución
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = self.select_parents()
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population


import matplotlib.pyplot as plt
from matplotlib import colors

class NQueensBacktrackingSolver:
    def __init__(self, n):
        self.n = n
        self.solution = None
        self.step = 0

    def is_safe(self, board, row, col):
        # Función para verificar si es seguro colocar una reina en la posición (row, col)
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(self, board, row):
        # Función recursiva para encontrar la primera solución
        if row == self.n:
            self.solution = list(board)
            return
        for col in range(self.n):
            self.step += 1
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve(board, row + 1)
                if self.solution:
                    return

    def find_solution(self):
        board = [-1] * self.n
        self.solve(board, 0)

    def run(self):
        self.find_solution()
        return self.solution, self.step
    
    def plot(self, board):
        chessboard = [[0 if (i+j) % 2 == 0 else 1 for j in range(self.n)] for i in range(self.n)]
        queens = [(row, col) for row, col in enumerate(board)]

        fig, ax = plt.subplots()
        cm = colors.ListedColormap(["white", "black"])

        for row, col in queens:
            color = "white" if chessboard[row][col] == 1 else "black"
            ax.text(row, col, "♛", ha="center", va="center", color=color, fontsize=20)
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(chessboard, cmap=cm)
        plt.show()

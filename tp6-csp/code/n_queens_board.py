import random
import matplotlib.pyplot as plt
from matplotlib import colors

class NQueensBoard:
    def __init__(self, n):
        self.n = n
        # Cada posicion corresponde a una columna y el valor al numero de fila donde se encuentra la reina.
        self.board = [random.randint(0, n-1) for _ in range(n)]

    def calculate_attack_pairs(self):
        attacks = 0
        for i in range(self.n):
            for j in range(i+1, self.n):
                if (self.board[i] == self.board[j] or
                    abs(self.board[i] - self.board[j]) == abs(i - j)):
                    attacks += 1
        return attacks

    def move_queen(self, row, new_col):
        self.board[row] = new_col
    
    def plot(self):
        chessboard = [[0 if (i+j) % 2 == 0 else 1 for j in range(self.n)] for i in range(self.n)]
        queens = [(row, col) for row, col in enumerate(self.board)]

        fig, ax = plt.subplots()
        cm = colors.ListedColormap(["white", "black"])

        for row, col in queens:
            color = "white" if chessboard[row][col] == 1 else "black"
            ax.text(row, col, "♛", ha="center", va="center", color=color, fontsize=20)
        
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(chessboard, cmap=cm)
        plt.show()

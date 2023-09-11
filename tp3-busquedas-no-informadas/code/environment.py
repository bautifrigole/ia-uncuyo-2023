from random import randint
from action import Action
import matplotlib.pyplot as plt
from matplotlib import colors

class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def is_equal_to(self, coord):
        return coord.x == self.x and coord.y == self.y
    
    def copy(self):
        return Coordinate(self.x, self.y)

class Environment:
    def __init__(self, size, obstacle_rate: float):
        self.matrix = [[0 for _ in range(size)] for _ in range(size)]
        self.size = size
        obstacle_slots = obstacle_rate * size * size
        self.fill_random_slots(obstacle_slots)

    def fill_random_slots(self, obstacle_slots: int):
        self.initial_position = Coordinate(randint(0, self.size-1), randint(0, self.size-1))
        self.goal_position = Coordinate(randint(0, self.size-1), randint(0, self.size-1))

        self.matrix[self.initial_position.x][self.initial_position.y] = 2
        self.matrix[self.goal_position.x][self.goal_position.y] = 3

        remaining_obstacle_slots = obstacle_slots
        while remaining_obstacle_slots > 0:
            coord = Coordinate(randint(0, self.size - 1), randint(0, self.size - 1))
            
            if (not self.matrix[coord.x][coord.y] == 1 and not self.is_initial_or_goal(coord)):
                self.matrix[coord.x][coord.y] = 1
                remaining_obstacle_slots -= 1
    
    def is_initial_or_goal(self, coord: Coordinate):
        return coord.is_equal_to(self.initial_position) or coord.is_equal_to(self.goal_position)
    
    def is_valid_action(self, action: Action, agent_coord: Coordinate):
        new_coord = agent_coord.copy()
        match action:
            case Action.DOWN:
                new_coord.y += 1
                return new_coord.y < self.size and not self.has_obstacle(new_coord)
            case Action.UP:
                new_coord.y -= 1
                return new_coord.y >= 0 and not self.has_obstacle(new_coord)
            case Action.RIGHT:
                new_coord.x += 1
                return new_coord.x < self.size and not self.has_obstacle(new_coord)
            case Action.LEFT:
                new_coord.x -= 1
                return new_coord.x >= 0 and not self.has_obstacle(new_coord)
            case _:
                return False
    
    def has_obstacle(self, coord: Coordinate):
        return self.matrix[coord.x][coord.y] == 1
    
    def get_neighbours(self, coord: Coordinate):
        neighbours = []
        if (self.is_valid_action(Action.DOWN, coord)):
            neighbours.append(Coordinate(coord.x, coord.y+1))
        if (self.is_valid_action(Action.UP, coord)):
            neighbours.append(Coordinate(coord.x, coord.y-1))
        if (self.is_valid_action(Action.RIGHT, coord)):
            neighbours.append(Coordinate(coord.x+1, coord.y))
        if (self.is_valid_action(Action.LEFT, coord)):
            neighbours.append(Coordinate(coord.x-1, coord.y))
        return neighbours
    
    def print_environment(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if (Coordinate(i,j).is_equal_to(self.initial_position)):
                    print("I", end="")
                elif (Coordinate(i,j).is_equal_to(self.goal_position)):
                    print("G", end="")
                else:
                    print(self.convert_character(self.matrix[i][j]), end="")
            print()

    def convert_character(self, char: int):
        if (char == 0):
            return "-"
        elif (char == 1):
            return "x"
    
    def plot(self):
        fig, ax = plt.subplots()

        cm = colors.ListedColormap(["white", "black", "lightblue", "red"])
        ax.matshow(self.matrix, cmap=cm)

        plt.show()

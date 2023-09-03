import random
from environment import Environment, Coordinate
from action import Action
import matplotlib.pyplot as plt
from matplotlib import colors

class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.actual_pos = env.initial_position
        self.remaining_actions = 1000
        self.visited_slots = []
        self.visited_slots.append(self.actual_pos.copy())

        while (not self.actual_pos.is_equal_to(env.goal_position) and self.remaining_actions > 0):
            self.think()
    
    def do_action(self, action: Action):
        if (not self.env.is_valid_action(action, self.actual_pos)):
            return
        
        new_coord = self.actual_pos.copy()

        match action:
            case Action.DOWN:
                new_coord.y += 1
            case Action.UP:
                new_coord.y -= 1
            case Action.RIGHT:
                new_coord.x += 1
            case Action.LEFT:
                new_coord.x -= 1
            case _:
                return False
        
        if (self.env.has_obstacle(new_coord)):
            return
        
        self.actual_pos = new_coord
        self.remaining_actions -= 1
        self.visited_slots.append(self.actual_pos.copy())

    def has_been_visited(self, coord: Coordinate):
        return any(coord.is_equal_to(v) for v in self.visited_slots)

    def think(self):
        action = random.choice(list(Action))
        self.do_action(action)
    
    def plotSolution(self):
        if self.visited_slots == []:
            return

        fig, ax = plt.subplots(figsize=(10, 10))

        m = self.env.matrix.copy()
        m[self.actual_pos.x][self.actual_pos.y] = 4

        for node in self.visited_slots[:-1]:
            m[node.x][node.y] = 5

        colorlist = ["white", "black", "green", "red", "lightblue", "pink"]
        cm = colors.ListedColormap(colorlist)

        ax.imshow(m, cmap=cm)
        plt.show()

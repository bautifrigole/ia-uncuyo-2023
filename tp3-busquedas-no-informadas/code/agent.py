import random
from environment import Environment, Coordinate
from action import Action
import matplotlib.pyplot as plt
from matplotlib import colors
from node import Node

class Agent:
    def __init__(self, env: Environment):
        self.env = env
        self.success = False
        self.steps = 0
        self.actual_pos = env.initial_position
        self.frontier = []
        self.explored = {}

    def search_path(self):
        start_node = Node(self.env.initial_position, 0, "visited")
        self.frontier.append(start_node)

        while self.frontier:
            node = self.extract_node()
            self.steps += 1

            if node.position.is_equal_to(self.env.goal_position):
                self.success = True
                return self.get_solution(node)

            if not self.has_been_explored(node.position):
                self.explored[(node.position.x, node.position.y)] = node

                children = [n for n in self.env.get_neighbours(node.position) if not self.has_been_explored(n) and not self.is_in_frontier(n)]
                for child in children:
                    new_node = Node(child, node.depth + 1, "unvisited", node)
                    self.add_node(new_node)

        return self.get_solution(None)

    def has_been_explored(self, coord: Coordinate):
        return (coord.x, coord.y) in self.explored

    def is_in_frontier(self, coord: Coordinate):
        return any(coord.is_equal_to(v.position) for v in self.frontier)        

    def extract_node(self):
        pass

    def add_node(self):
        pass

    def get_solution(self, node: Node):
        self.path = []
        if node is None:
            return (self.__class__.__name__, [], self.steps, float("inf"), self.success, self.env.size)
        depth = node.depth
        while node.parent != None:
            self.path.append(node.position)
            node = node.parent
        self.path.reverse()
        return (self.__class__.__name__, self.path, self.steps, depth, self.success, self.env.size)
    
    def plot_solution(self):
        if self.path == []:
            return

        fig, ax = plt.subplots(figsize=(10, 10))

        m = self.env.matrix.copy()
        m[self.actual_pos.x][self.actual_pos.y] = 4

        for node in self.path[:-1]:
            m[node.x][node.y] = 5

        cm = colors.ListedColormap(["white", "black", "green", "red", "lightblue", "pink"])

        ax.imshow(m, cmap=cm)
        plt.show()

class BFSAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)

    def extract_node(self):
        return self.frontier.pop(0)
    
    def add_node(self, node: Node):
        self.frontier.append(node)

class DFSAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)

    def extract_node(self):
        return self.frontier.pop()
    
    def add_node(self, node: Node):
        self.frontier.append(node)
import random
import copy
from environment import Environment, Coordinate
from action import Action
import matplotlib.pyplot as plt
import heapq
from matplotlib import colors
from node import Node, UniformNode
from priority_queue import PriorityQueue

class Agent():
    def __init__(self, env: Environment):
        self.env = env
        self.success = False
        self.steps = 0
        self.actual_pos = env.initial_position
        self.frontier = []
        self.explored = {}
    
    def create_node(self, coord: Coordinate, depth: int, parent: Node =None):
        return Node(coord, depth, parent)

    def search_path(self):
        start_node = self.create_node(self.env.initial_position, 0)
        self.add_node(start_node)

        while self.frontier:
            node = self.extract_node()
            self.steps += 1

            if node.position.is_equal_to(self.env.goal_position):
                self.success = True
                return self.get_solution(node)

            if not self.has_been_explored(node.position):
                self.explored[(node.position.x, node.position.y)] = node

                children = [n for n in self.env.get_neighbours(node.position) if not self.has_been_explored(n)]
                for child in children:
                    new_node = self.create_node(child, node.depth + 1, node)
                    self.add_node(new_node)
            else:
                self.update_explored(node)

        return self.get_solution(None)

    def has_been_explored(self, coord: Coordinate):
        return (coord.x, coord.y) in self.explored

    def is_in_frontier(self, coord: Coordinate):
        return any(coord.is_equal_to(v.position) for v in self.frontier)        

    def extract_node(self):
        pass

    def add_node(self):
        pass

    def update_explored(self, node: Node):
        pass

    def get_solution(self, node: Node):
        self.path = []
        if node is None:
            return (self.__class__.__name__, [], self.steps, "depth: inf", self.success)
        depth = node.depth
        while node.parent != None:
            self.path.append(node.position)
            node = node.parent
        self.path.reverse()
        return (self.__class__.__name__, self.path, self.steps, "depth: "+str(depth), self.success)
    
    def plot_solution(self):
        if self.path == []:
            return
        
        fig, ax = plt.subplots(figsize=(10, 10))

        m = copy.deepcopy(self.env.matrix)

        for node in self.path[:-1]:
            m[node.x][node.y] = 4

        cm = colors.ListedColormap(["white", "black", "red", "green", "lightblue"])

        ax.imshow(m, cmap=cm)
        plt.title(self.__class__.__name__)
        plt.savefig("./tp4-busquedas-informadas/plots/"+self.__class__.__name__+".png")
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

class LimitedDFSAgent(DFSAgent):
    def __init__(self, env: Environment, limit: int):
        super().__init__(env)
        self.limit = limit
    
    def add_node(self, node: Node):
        if node.depth <= self.limit:
            self.frontier.append(node)

class UniformCostAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)
        self.frontier = PriorityQueue()
    
    def create_node(self, coord: Coordinate, depth: int, parent: Node =None):
        cost = 0 if parent is None else parent.cost + 1
        return UniformNode(coord, depth, parent, cost)

    def extract_node(self):
        return self.frontier.pop()
    
    def add_node(self, node: Node):
        self.frontier.insert(node)
    
    def update_explored(self, node: Node):
        if node.cost < self.explored[(node.position.x, node.position.y)].cost:
            self.explored[(node.position.x, node.position.y)] = node

class AStarAgent(Agent):
    def __init__(self, env: Environment):
        super().__init__(env)
    
    def create_node(self, coord: Coordinate, depth: int, parent: Node =None, cost=0, heuristic=0):
        cost = 0 if parent is None else parent.cost + 1
        return UniformNode(coord, depth, parent, cost, heuristic)

    def extract_node(self):
        return heapq.heappop(self.frontier)
    
    def add_node(self, node: Node):
        heapq.heappush(self.frontier, (node.total_cost(), node))
    
    def update_explored(self, node: Node):
        if node.cost < self.explored[(node.position.x, node.position.y)].cost:
            self.explored[(node.position.x, node.position.y)] = node
    
    def search_path(self):
        return self.astar_search()
    
    def astar_search(self):
        start_node = self.create_node(self.env.initial_position, 0, None, cost=0, heuristic=self.heuristic(self.env.initial_position, self.env.goal_position))
        self.add_node(start_node)

        while self.frontier:
            _, node = self.extract_node()
            self.steps += 1

            if node.position.is_equal_to(self.env.goal_position):
                self.success = True
                return self.get_solution(node)

            if not self.has_been_explored(node.position):
                self.explored[(node.position.x, node.position.y)] = node

                children = [n for n in self.env.get_neighbours(node.position) if not self.has_been_explored(n)]
                for child in children:
                    child_cost = node.cost + 1
                    new_node = self.create_node(child, node.depth + 1, node, child_cost, self.heuristic(child, self.env.goal_position))
                    self.add_node(new_node)
            else:
                self.update_explored(node)

        return self.get_solution(None)

    def heuristic(self, actual_coord: Coordinate, goal_coord: Coordinate):
        # Manhattan Distance
        return abs(actual_coord.x - goal_coord.x) + abs(actual_coord.y - goal_coord.y)

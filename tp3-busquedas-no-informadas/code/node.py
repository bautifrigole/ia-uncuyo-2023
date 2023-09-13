from environment import Coordinate

class Node:
    def __init__(self, coord: Coordinate, depth=None, parent=None):
        self.position = coord
        self.parent = parent
        self.depth = depth

class UniformNode(Node):
    def __init__(self, coord: Coordinate, depth=None, parent=None, cost=0):
        super().__init__(coord, depth, parent)
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash((self.position, self.cost))

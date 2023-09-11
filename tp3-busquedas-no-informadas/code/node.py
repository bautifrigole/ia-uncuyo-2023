from environment import Coordinate

class Node:
    def __init__(self, coord: Coordinate, depth=None, status=None, parent=None):
        self.position = coord
        self.parent = parent
        self.depth = depth
        self.status = status

from enum import Enum

class Action(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def __str__(self):
        return self.name

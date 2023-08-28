import random
from environment import Action, Environment

class Agent:
    def __init__(self, env: Environment, initial_posX, initial_posY, is_random_agent=False):
        self.env = env
        self.posX = initial_posX
        self.posY = initial_posY
        self.points = 0
        self.remaining_actions = 1000
        self.is_random_agent = is_random_agent

        while (env.remaining_dirty_slots > 0 and self.remaining_actions > 0):
            self.think()
    
    def do_action(self, action: Action):
        if (not self.env.validate_action(self, action)):
            return
        
        match action:
            case Action.DOWN:
                self.posY += 1
            case Action.UP:
                self.posY -= 1
            case Action.RIGHT:
                self.posX += 1
            case Action.LEFT:
                self.posX -= 1
            case Action.CLEAN:
                if(self.is_slot_dirty()):
                    self.points += 1
                self.env.clean_slot(self.posX, self.posY)
        
        self.remaining_actions -= 1
            

    def is_slot_dirty(self):
        return self.env.is_dirty(self.posX, self.posY)

    def think(self):
        if (self.is_random_agent):
            self.do_action(random.choice(list(Action)))
        else: 
            if(self.is_slot_dirty()):
                self.do_action(Action.CLEAN)
            else:
                directions = [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]
                self.do_action(random.choice(directions))

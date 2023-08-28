from random import randint
from agent import Agent
from environment import Environment

env = Environment(5, 5, 0.5)
env.print_environment()
print()
agent = Agent(env, randint(0, env.sizeX-1), randint(0, env.sizeY-1), True)
env.print_environment()
print()
print("remaining_actions: ", agent.remaining_actions)
print("points: ", agent.points)

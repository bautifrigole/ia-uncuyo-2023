from environment import Environment, Coordinate
from agent import Agent

size = 50
env = Environment(size, Coordinate(0,0), Coordinate(49,49), 0.08)
print()

agent = Agent(env)
print(agent.remaining_actions)
agent.plotSolution()

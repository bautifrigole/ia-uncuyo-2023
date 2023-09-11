from environment import Environment, Coordinate
from agent import *

size = 20
env = Environment(size, 0.08)
env.plot()
print()

bfs_agent = BFSAgent(env)
print(bfs_agent.search_path())
bfs_agent.plot_solution()

dfs_agent = DFSAgent(env)
print(dfs_agent.search_path())
dfs_agent.plot_solution()

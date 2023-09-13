from environment import Environment, Coordinate
from agent import *

size = 20
env = Environment(size, 0.08)

bfs_agent = BFSAgent(env)
print(bfs_agent.search_path())
bfs_agent.plot_solution()

print()

dfs_agent = DFSAgent(env)
print(dfs_agent.search_path())
dfs_agent.plot_solution()

print()

limited_dfs_agent = LimitedDFSAgent(env, 40)
print(limited_dfs_agent.search_path())
limited_dfs_agent.plot_solution()

print()

uniform_cost_agent = UniformCostAgent(env)
print(uniform_cost_agent.search_path())
uniform_cost_agent.plot_solution()
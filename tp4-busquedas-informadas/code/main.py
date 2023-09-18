from environment import Environment
from agent import *
import matplotlib.pyplot as plt
import csv

size = 100
results = { 
    "bfs": [],
    "dfs": [],
    "limited_dfs": [],
    "uniform_cost": [],
    "astar": []
}

for i in range(30):
    env = Environment(size, 0.08)

    agent = BFSAgent(env)
    solution = agent.search_path()
    results["bfs"].append(len(agent.explored))

    agent = DFSAgent(env)
    solution = agent.search_path()
    results["dfs"].append(len(agent.explored))

    agent = LimitedDFSAgent(env, 200)
    solution = agent.search_path()
    results["limited_dfs"].append(len(agent.explored))

    agent = UniformCostAgent(env)
    solution = agent.search_path()
    results["uniform_cost"].append(len(agent.explored))

    agent = AStarAgent(env)
    solution = agent.search_path()
    results["astar"].append(len(agent.explored))

    print(i)

# Crear un gráfico de cajas para cada algoritmo
fig, ax = plt.subplots()

# Configurar propiedades del gráfico de cajas
boxprops = dict(linewidth=2, color='blue')
whiskerprops = dict(linestyle='--', linewidth=1, color='green')
medianprops = dict(linewidth=2, color='red')

# Crear el gráfico de cajas combinado
ax.boxplot(results.values(), labels=results.keys(),
           boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops)

# Agregar título y etiquetas de ejes
plt.title('Comparación de Algoritmos de Búsqueda')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Cantidad de Nodos Explorados')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

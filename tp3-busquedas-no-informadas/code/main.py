from environment import Environment
from agent import *
import matplotlib.pyplot as plt
import csv

size = 100
results = { 
    "bfs": [],
    "dfs": [],
    "limited_dfs": [],
    "uniform_cost": []
}

with open('./tp3-busquedas-no-informadas/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Algorithm_name", "env_n", "estates_n", "solution_found"])

    for i in range(30):
        writer = csv.writer(file)
        env = Environment(size, 0.08)

        agent = BFSAgent(env)
        solution = agent.search_path()
        writer.writerow([solution[0], i, len(agent.explored), agent.success])
        results["bfs"].append(len(agent.explored))

        agent = DFSAgent(env)
        solution = agent.search_path()
        writer.writerow([solution[0], i, len(agent.explored), agent.success])
        results["dfs"].append(len(agent.explored))

        agent = LimitedDFSAgent(env, 200)
        solution = agent.search_path()
        writer.writerow([solution[0], i, len(agent.explored), agent.success])
        results["limited_dfs"].append(len(agent.explored))

        agent = UniformCostAgent(env)
        solution = agent.search_path()
        writer.writerow([solution[0], i, len(agent.explored), agent.success])
        results["uniform_cost"].append(len(agent.explored))
        print(i)

file.close()

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

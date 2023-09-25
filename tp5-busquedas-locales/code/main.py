from n_queens_solver import *
import time
import csv
import matplotlib.pyplot as plt

n_values = [4, 8, 10]
max_evaluations = 10000
results = { 
    "hill-climbing": [],
    "simulated-annealing": [],
    "genetic": []
}

with open('./tp5-busquedas-locales/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Algorithm_Name", "Queens", "Iterations", "Time", "H_Value", "Solution_Found"])
    for i in range(10):
        print(i)
        writer = csv.writer(file)

        for n in n_values:
            print(f"Solving {n}-Queens:")

            print("hill-climbing")
            initial_time = time.time()
            solver = HillClimbingSolver(n, max_evaluations)
            board, attacks, evaluations = solver.solve()
            final_time = time.time()
            result = ["hill-climbing", n, evaluations, final_time - initial_time, attacks, attacks == 0]
            results["hill-climbing"].append(result)
            writer.writerow(result)

            print("simulated-annealing")
            initial_time = time.time()
            solverS = SimulatedAnnealingSolver(n, max_evaluations, 100.0, 0.95)
            board, attacks, evaluations = solver.solve()
            final_time = time.time()
            result = ["simulated-annealing", n, evaluations, final_time - initial_time, attacks, attacks == 0]
            results["simulated-annealing"].append(result)
            writer.writerow(result)

            print("genetic")
            initial_time = time.time()
            solver = GeneticAlgorithmSolver(n, population_size=50, generations=500, mutation_rate=0.8)
            board, attacks, evaluations = solver.solve()
            final_time = time.time()
            result = ["genetic", n, evaluations, final_time - initial_time, attacks, attacks == 0]
            results["genetic"].append(result)
            writer.writerow(result)

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
plt.title('Comparación de Algoritmos de Búsqueda Local')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Cantidad de Nodos Explorados')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
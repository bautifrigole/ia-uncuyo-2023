from n_queens_solver import *
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

n_values = [4, 8, 10, 12, 15]
iterations = 30
max_evaluations = 10000
results = { 
    "hill-climbing": [],
    "simulated-annealing": [],
    "genetic": []
}

with open('./tp5-busquedas-locales/results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Algorithm_Name", "Queens", "Iterations", "Time", "H_Value", "Solution_Found"])
    for i in range(iterations):
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
            solver = SimulatedAnnealingSolver(n, max_evaluations, 100.0, 0.95)
            board, attacks, evaluations = solver.solve()
            final_time = time.time()
            result = ["simulated-annealing", n, evaluations, final_time - initial_time, attacks, attacks == 0]
            results["simulated-annealing"].append(result)
            writer.writerow(result)

            print("genetic")
            initial_time = time.time()
            solver = GeneticAlgorithmSolver(n, population_size=7, generations=380, mutation_rate=0.4)
            board, attacks, evaluations = solver.solve()
            final_time = time.time()
            result = ["genetic", n, evaluations, final_time - initial_time, attacks, attacks == 0]
            results["genetic"].append(result)
            writer.writerow(result)
        print("")

file.close()



# Inicializa contadores para cada algoritmo
optimal_counts = {
    "hill-climbing": 0,
    "simulated-annealing": 0,
    "genetic": 0
}

# Itera sobre los resultados de cada algoritmo
for algorithm in results:
    for result in results[algorithm]:
        if result[5]:  # Comprueba si attacks es igual a 0
            optimal_counts[algorithm] += 1

# Calcula el porcentaje de veces que se llega a un estado óptimo
total_runs = iterations*len(n_values)
optimal_percentages = {algorithm: (count / total_runs) * 100 for algorithm, count in optimal_counts.items()}

# Imprime los porcentajes
for algorithm, percentage in optimal_percentages.items():
    print(f"{algorithm}: {percentage:.2f}% de soluciones óptimas")
print("")



# Crear un gráfico de cajas para cada algoritmo
fig, ax = plt.subplots()

# Configurar propiedades del gráfico de cajas
boxprops = dict(linewidth=2, color='blue')
whiskerprops = dict(linestyle='--', linewidth=1, color='green')
medianprops = dict(linewidth=2, color='red')

execution_times = {
    algorithm: [result[3] for result in results_list] for algorithm, results_list in results.items()
}

# Crear el gráfico de cajas combinado
ax.boxplot(execution_times.values(), labels=results.keys(),
           boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops)

# Agregar título y etiquetas de ejes
plt.title('Comparación de Algoritmos de Búsqueda Local')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Tiempo de ejecución')

# Mostrar el gráfico
plt.tight_layout()
plt.show()



# Inicializa listas para almacenar evaluaciones por algoritmo
evaluations_by_algorithm = {
    "hill-climbing": [],
    "simulated-annealing": [],
    "genetic": []
}

# Llena las listas con las evaluaciones de cada ejecución
for algorithm in results:
    for result in results[algorithm]:
        evaluations_by_algorithm[algorithm].append(result[2])  # 2 es el índice de evaluations en el resultado

# Calcula la cantidad promedio de estados previos y su desviación estándar
avg_evaluations = {algorithm: np.mean(evaluations) for algorithm, evaluations in evaluations_by_algorithm.items()}
std_dev_evaluations = {algorithm: np.std(evaluations) for algorithm, evaluations in evaluations_by_algorithm.items()}

# Imprime los resultados
for algorithm in results:
    print(f"{algorithm}:")
    print(f"Cantidad promedio de estados previos: {avg_evaluations[algorithm]:.2f}")
    print(f"Desviación estándar de estados previos: {std_dev_evaluations[algorithm]:.2f}")
    print("")



"""# Supongamos que tienes los datos de evaluaciones para un algoritmo específico en una lista llamada 'evaluations'
evaluations = results["hill-climbing"][2][2]  # Reemplaza "hill-climbing" con el nombre de tu algoritmo

# Supongamos que también tienes los valores de cantidad de ataques (h) en cada iteración en una lista llamada 'attack_values'
attack_values = results["hill-climbing"][2][6]

# Crea un gráfico de línea para mostrar la variación de h a lo largo de las iteraciones
plt.plot( np.arange(1,evaluations+1), attack_values, marker='o', linestyle='-')

# Agrega título y etiquetas de ejes
plt.title('Variación de h() a lo largo de las Iteraciones (Hill Climbing) con 10 reinas')
plt.xlabel('Iteraciones')
plt.ylabel('Valor de h()')

# Muestra el gráfico
plt.grid(True)
plt.show()"""

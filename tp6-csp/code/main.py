from backtracking import NQueensBacktrackingSolver
from forward_checking import NQueensForwardCheckingSolver
import time
import numpy as np
import matplotlib.pyplot as plt

n_values = [4, 8, 10, 12, 15]
iterations = 30
results = {
    "backtracking": [],
    "forward-checking": []
}

for i in range(iterations):
    print(i)

    for n in n_values:
        print(f"Solving {n}-Queens:")

        print("Backtracking")
        initial_time = time.time()
        solver = NQueensBacktrackingSolver(n)
        board, steps = solver.run()
        final_time = time.time()
        result = ["backtracking", n, steps, final_time - initial_time]
        print("Steps: ", steps)
        results["backtracking"].append(result)

        print("Forward Checking")
        initial_time = time.time()
        solver = NQueensForwardCheckingSolver(n)
        board, steps = solver.run()
        final_time = time.time()
        result = ["forward-checking", n, steps, final_time - initial_time]
        print("Steps: ", steps)
        results["forward-checking"].append(result)

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
plt.title('Comparación de Algoritmos CSP')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Tiempo de ejecución')

# Mostrar el gráfico
plt.tight_layout()
plt.show()



# Crear un gráfico de cajas para cada algoritmo
fig2, ax2 = plt.subplots()

# Configurar propiedades del gráfico de cajas
boxprops = dict(linewidth=2, color='blue')
whiskerprops = dict(linestyle='--', linewidth=1, color='green')
medianprops = dict(linewidth=2, color='red')

steps = {
    algorithm: [result[2] for result in results_list] for algorithm, results_list in results.items()
}

# Crear el gráfico de cajas combinado
ax2.boxplot(steps.values(), labels=results.keys(),
           boxprops=boxprops, whiskerprops=whiskerprops, medianprops=medianprops)

# Agregar título y etiquetas de ejes
plt.title('Comparación de Algoritmos CSP')
plt.xlabel('Algoritmo de Búsqueda')
plt.ylabel('Pasos para encontrar la solución')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

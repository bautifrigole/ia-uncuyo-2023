from random import randint
from agent import Agent
from environment import Environment
import matplotlib.pyplot as plt
import numpy as np

environment_sizes = [2, 4, 8, 16, 32, 64, 128]
dirt_rates = [0.1, 0.2, 0.4, 0.8]
repeating_amount = 10
results = []

for i in range(len(environment_sizes)):
    size = environment_sizes[i]
    row = []

    for j in range(len(dirt_rates)):
        moves = []
        points = []

        for _ in range(repeating_amount):
            env = Environment(size, size, dirt_rates[j])
            agent = Agent(env, randint(0, env.sizeX-1), randint(0, env.sizeY-1), False)
            moves.append(1000-agent.remaining_actions)
            points.append(agent.points)

        avgMoves = sum(moves) / len(moves)
        avgPoints = sum(points) / len(points)
        row.append([avgPoints, avgMoves])

    results.append(row)


# Gráficos de barras
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

colors = ['#E1B16A', '#A47848', '#725636', '#452620']
bar_width = 0.2
x_positions = np.arange(len(environment_sizes))

for i, dirt_rate in enumerate(dirt_rates):
    movements = [result[i][1] for result in results]
    points = [result[i][0] for result in results]

    ax.bar(x_positions + i * bar_width, movements, bar_width, label=f'Suciedad {dirt_rate}', color=colors[i])
    ax2.bar(x_positions + i * bar_width, points, bar_width, label=f'Suciedad {dirt_rate}', color=colors[i])

ax.set_xlabel('Tamaño del Entorno')
ax.set_ylabel('Cantidad de Movimientos Promedio')
ax.set_title('Cantidad de Movimientos Promedio por Tamaño de Entorno y Nivel de Suciedad con un Agente Reflexivo')
ax.set_xticks(x_positions + bar_width * (len(dirt_rates) - 1) / 2)
ax.set_xticklabels(environment_sizes)
ax.legend()

ax2.set_xlabel('Tamaño del Entorno')
ax2.set_ylabel('Cantidad de Puntos Promedio')
ax2.set_title('Cantidad de Puntos Promedio por Tamaño de Entorno y Nivel de Suciedad con un Agente Reflexivo')
ax2.set_xticks(x_positions + bar_width * (len(dirt_rates) - 1) / 2)
ax2.set_xticklabels(environment_sizes)
ax2.legend()
ax2.set_ylim(0, 250)

plt.tight_layout()
plt.show()

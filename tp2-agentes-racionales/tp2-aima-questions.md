### 2.10 Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

#### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, ya que no tiene conocimiento del estado de todo el entorno, es decir, no sabe qué casilleros están sucios hasta estar parado en él. Tampoco tiene memoria de los casilleros por los que ya pasó, estas restricciones hacen que el agente no sea perfectamente racional.

#### b. What about a reflex agent with state? Design such an agent.

Si este agente tuviese memoria de los casilleros por los que ya pasó, tampoco sería perfectamente racional ya que sigue sin tener conocimiento previo total del entorno.

#### c. How do your answers to a and b change if the agent’s percepts give it the clean/dirty status of every square in the environment?

Si el agente tuviese conocimiento del estado de todo el entorno y memoria de los casilleros por los que ya pasó, se podría construir un agente perfectamente racional, ya que podría buscar los caminos más cortos (con menos movimientos) hacia los casilleros sucios y sin repetir por los que ya pasó.

### 2.11 Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)

#### a. Can a simple reflex agent be perfectly rational for this environment? Explain.

No, si se desconoce la geografía del entorno (su extensión, límites y obstáculos) no podría ser perfectamente racional, ya que no cumple con las dos condiciones anteriores (tener conocimiento del estado de todo el entorno y memoria de los casilleros por los que ya pasó) y además tampoco sabe de las dimensiones del entorno, por lo tanto, llevaría más movimientos explorar el entorno desconocido (considerando que se tiene una cantidad de movimientos limitada).

#### b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.

A partir de los resultados de los ejercicios [D](./tp2-results.md) y [E](./tp2-results.md), se puede observar que el rendimiento del agente aleatorio es bastante similar al reflexivo en entornos pequeños, pero a medida que se empieza a agrandar el entorno, el agente aleatorio pasa a ser bastante inferior al reflexivo.

#### c. Can you design an environment in which your randomized agent will perform poorly? Show your results.

Como se mencionó anteriormente, el agente aleatorio tiene rendimientos bajos en los entornos de gran tamaño, y si además le sumamos baja probabilidad de que un casillero esté sucio (pocos casilleros sucios en un entorno muy grande), el desempeño se ve afectado aún más.

#### d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?

Sí, es probable que un agente reflexivo que cuenta con memoria de los casilleros que ya visitó tenga mejor desempeño que uno que no lo hace. Sin embargo, sigue sin tener conocimiento total de los estados de los casilleros, por lo que también deberá hacer muchos movimientos para encontrarlos en primer lugar.

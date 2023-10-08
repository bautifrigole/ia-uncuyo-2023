### 1. Describir en detalle una formulación CSP para el Sudoku.

- Variables: {c00, c01, ..., cij, ..., c88}
- Dominios: Dij={1, ..., 9}.
- Restricciones: un número solamente puede aparecer una vez
    - en cada fila
    - en cada columna
    - en cada región

### 2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema de colorear el mapa de Australia (Figura 5.1 AIMA 2da edición).

Problema y sus restricciones:

- Variables: {WA, NT, Q, NSW, V, SA, T}

- Dominios:
  - WA = {red}
  - NT = {red, green, blue}
  - Q = {red, green, blue}
  - NSW = {red, green, blue}
  - V = {blue}
  - SA = {red, green, blue}
  - T = {red, green, blue}

- Restricciones: Dos estados adyacentes no pueden tener el mismo color.

Comenzamos inicializando una cola con todas las restricciones (arcos) del problema: {(SA, WA), (SA, NT), (SA, Q), (SA, NSW), (SA, V), (NT, WA), (NT, Q), (NT, SA), (Q, NSW), (Q, NT), (Q, SA), ...}

Se analizan los arcos que parten de SA. Tomamos el arco (SA, WA), y los dominios quedan así:

- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green, blue}
- T = {red, green, blue}

Se agregan los arcos (WA, SA) y (V, SA) a la cola de arcos a analizar. 
Tomamos el arco (SA, V), y los dominios quedan así:

- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, green, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Tomamos el arco (SA, NSW), y los dominios quedan así:

- WA = {red}
- NT = {red, green, blue}
- Q = {red, green, blue}
- NSW = {red, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Tomamos el arco (NT, WA), y los dominios quedan así:

- WA = {red}
- NT = {green, blue}
- Q = {red, green, blue}
- NSW = {red, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Se agrega el arco (WA, NT) a la cola.
Tomamos el arco (NT, SA), y los dominios quedan así:

- WA = {red}
- NT = {blue}
- Q = {red, green, blue}
- NSW = {red, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Tomamos el arco (NT, Q), y los dominios quedan así:

- WA = {red}
- NT = {blue}
- Q = {red, green}
- NSW = {red, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Tomamos el arco (SA, Q), y los dominios quedan así:

- WA = {red}
- NT = {blue}
- Q = {red}
- NSW = {red, blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Tomamos el arco (Q, NSW), y los dominios quedan así:

- WA = {red}
- NT = {blue}
- Q = {red}
- NSW = {blue}
- V = {blue}
- SA = {green}
- T = {red, green, blue}

Si tomamos el arco (V, NSW) y eliminamos "blue" del dominio de NSW, el dominio de NSW quedaría vacío. Esto indica que la asignación parcial {WA=red, V=blue} no es consistente.

### 3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualesquiera dos variables están relacionadas por a lo sumo un camino).

La complejidad en el peor caso es de O(n^2 * d^3), donde n representa el número de variables y d el tamaño máximo del dominio de cualquier variable en el problema CSP.

Cada variable está relacionada con a lo sumo una variable a lo largo de un único camino. Por lo tanto, en el peor caso, para cada variable, se deben examinar todas las restricciones con todas las otras variables en el camino hacia arriba y hacia abajo en el árbol de restricciones. Esto lleva a un factor de n^2.

Además, para cada par de variables que están relacionadas a lo largo de este camino, se deben realizar comparaciones y posibles eliminaciones en los dominios de esas variables. La complejidad de esta parte es O(d^3), ya que puede requerir un bucle triple para verificar todas las combinaciones de valores en los dominios de las variables relacionadas.

### 4. AC-3 coloca de nuevo en la cola todo arco (Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Supongamos que por cada arco (Xk, Xi) se puede llevar la cuenta del número de valores restantes de Xi que sean consistentes con cada valor de Xk. Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n^2d^2).

Podemos utilizar una matriz, donde las filas representan los valores de Xk y las columnas representan los valores de Xi. Inicialmente, la matriz se llena con ceros.

A medida que aplicamos el algoritmo AC-3 y realizamos restricciones, se actualiza la matriz cuando se elimina un valor del dominio de Xi. De esta manera, estamos manteniendo un seguimiento eficiente de cuántos valores de Xi son consistentes con cada valor de Xk. Esto nos permite determinar si el arco (Xk, Xi) es consistente sin tener que realizar comparaciones costosas cada vez que se actualiza.

La complejidad temporal de esta implementación es O(n^2 * d^2), donde n representa el número de variables, cada una con un dominio máximo de tamaño d. Esto es porque debemos considerar cada par de variables (Xk, Xi) y cada combinación de valores en sus dominios.

### 5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar:

a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)

b. Argumentar por qué lo demostrado en a. es suficiente.

**Demostración:**

Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol y hemos logrado la 2-consistencia. Esto significa que para cada par de variables (Xi, Xj) en el CSP, cualquier valor en el dominio de Xi es consistente con al menos un valor en el dominio de Xj, y viceversa.

Para demostrar la n-consistencia, consideremos cualquier variable Xi en el CSP. Dado que el grafo de restricciones es un árbol, Xi está relacionada con el resto de las variables a través de un único camino en el árbol. Denotemos las variables en este camino como X1, X2, ..., Xn, donde X1 = Xi.

Dado que hemos logrado la 2-consistencia, sabemos que para cualquier variable Xk en el camino (donde k > 1), hay al menos un valor en el dominio de Xk que es consistente con algún valor en el dominio de Xk-1. Esto es cierto para todas las variables en el camino.

Por lo tanto, hemos demostrado que para cualquier variable Xi en el CSP, cualquier valor en su dominio es consistente con al menos un valor en el dominio de cada otra variable en el CSP, siguiendo el único camino en el árbol de restricciones.

Este resultado es suficiente porque, en un CSP, el objetivo es encontrar una asignación que cumpla con todas las restricciones. Si hemos logrado que todas las variables sean consistentes entre sí, hemos eliminado cualquier conflicto y hemos asegurado que existe una solución que satisface todas las restricciones. Esto es fundamental para la correctitud del algoritmo CSP en árboles estructurados, ya que garantiza que si una solución existe, el algoritmo la encontrará.

### 6. Implementar una solución al problema de las n-reinas utilizando una formulación CSP
    a. Implementar una solución utilizando backtracking
    b. Implementar una solución utilizando encadenamiento hacia adelante.
    c. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10,
    12 y 15 reinas.
    d. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la
    solución para los casos de 4, 8, 10, 12 y 15 reinas.
    e. Realizar un gráfico de cajas para los puntos c y d.

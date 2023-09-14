### B) Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio con una tasa de obstáculos del 8 por ciento, calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino (si es que fue posible). Evaluar cada uno de los algoritmos sobre el mismo conjunto de datos generado.  Presentar los resultados en un gráfico de cajas y bigotes o boxplots.

![BoxPlot](https://github.com/bautifrigole/ia-uncuyo-2023/blob/develop/tp3-busquedas-no-informadas/plots/BoxPlot.png)

### C) Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.

En mi opinión, considero que el algoritmo más apropiado para abordar este problema es el BFS. Este algoritmo no solo es capaz de encontrar la solución óptima, sino que también presenta una diferencia moderada en la cantidad de nodos explorados en comparación con otros algoritmos. No obstante, si se busca una solución subóptima que involucre la exploración de un número menor de nodos, el DFS limitado podría constituir una alternativa viable. Es importante destacar que la efectividad del DFS limitado dependerá del límite que se establezca, ya que podría o no alcanzar la solución deseada.

### Gráficos

![BFS](https://github.com/bautifrigole/ia-uncuyo-2023/blob/develop/tp3-busquedas-no-informadas/plots/BFSAgent.png)
![DFS](https://github.com/bautifrigole/ia-uncuyo-2023/blob/develop/tp3-busquedas-no-informadas/plots/DFSAgent.png)
![LimitedDFS](https://github.com/bautifrigole/ia-uncuyo-2023/blob/develop/tp3-busquedas-no-informadas/plots/LimitedDFSAgent.png)
![UniformCost](https://github.com/bautifrigole/ia-uncuyo-2023/blob/develop/tp3-busquedas-no-informadas/plots/UniformCostAgent.png)

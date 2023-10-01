## Parte II

### N Reinas
![8-Queens](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/1578cdff-65ca-40b0-ae65-4548fde0403e)

### A) Resultados obtenidos

![BoxPlot](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/50c5954e-5459-4bab-aaf4-fa49185e36e4)

![results](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/9de35511-7fc9-4208-9d6d-0ec454b58e8d)

(En el algoritmo genético se tomó cada generación como un estado)

### B) Variación de la función h() a lo largo de las iteraciones

#### Hill Climbing
![H_HillClimbing](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/d9bed5fd-3b5e-4ad5-a734-82eaa56dac7e)

#### Simulated Annealing
![H_SimulatedAnnealing](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/84d85775-4298-4df9-b290-79a2e8324f17)

#### Genetic

En el algoritmo genético se implementaron los siguientes operadores:
- **Seleccion**: Torneos de 4 participantes
- **Crossover**: Crossover de un punto aleatorio
- **Mutacion**: Mutacion de un gen aleatorio
- **Reemplazo**: Elitismo

![H_Genetic](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/f5334446-4476-4a99-a219-ea02b32ace05)

### C) Indicar según su criterio, cuál de los tres algoritmos implementados resulta más adecuado para la solución del problema de las n-reinas. Justificar.

Depende según nuestro caso particular, si queremos obtener un caso óptimo y no nos importa que demore en encontrar la solución, un algoritmo genético sería la mejor opción, pudiendo incluso mejorar los resultados obtenidos al seguir modificando valores de los distintos parámetros. Ahora si queremos que el problema se resuelva rápido y no nos interesa obtener un caso óptimo, tanto Hill Climbing como Simulated Annealing son muy buenas opciones para este caso, pero me inclinaría más por Hill Climbing ya que en mis resultados obtuvo un mayor porcentaje de soluciones óptimas y, en promedio, recorriendo menos estados.

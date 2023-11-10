### 1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible statistical learning method to be better or worse than an inflexible method. Justify your answer.

#### (a) The sample size n is extremely large, and the number of predictors p is small.

En este caso, generalmente esperaríamos que el rendimiento de un método flexible sea peor al de un método inflexible. Con un tamaño de muestra extremadamente grande, los métodos flexibles pueden aprender patrones complejos en los datos, pero también existe el riesgo de overfitting. Un método más inflexible podría ser preferible ya que podría ser menos propenso a overfittear pequeños detalles de los datos.

#### (b) The number of predictors p is extremely large, and the number of observations n is small.

En este caso, esperaríamos que el rendimiento de un método flexible sea mejor que el de un método inflexible. Con un número extremadamente grande de predictores y un tamaño de muestra pequeño, un método flexible puede ser más capaz de capturar relaciones complejas en los datos, mientras que un método inflexible podría no ser lo suficientemente complejo como para modelar la variabilidad.

#### (c) The relationship between the predictors and response is highly non-linear.

En este caso, esperaríamos que el rendimiento de un método flexible sea mejor que el de un método inflexible. Los métodos flexibles, como los modelos no lineales, pueden capturar relaciones no lineales de manera más efectiva, mientras que los métodos inflexibles podrían tener dificultades para modelar patrones no lineales.

#### (d) The variance of the error terms, i.e. σ^2 = Var(ϵ), is extremely high.

Dado que el error irreducible es muy alto, no sería conveniente utilizar un método extremadamente flexible, ya que podría realizar sobreajuste sobre el ruido en lugar de capturar patrones reales. Como regla general, al usar métodos flexibles, aumenta la varianza. Por lo tanto, lo ideal sería buscar un método flexible pero más restrictivo al mismo tiempo para disminuir la varianza sin aumentar demasiado el sesgo.

### 2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested in inference or prediction. Finally, provide n and p.

#### (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, industry and the CEO salary. We are interested in understanding which factors aﬀect CEO salary.

Tipo de Problema: Regresión.

Interés Principal: Inferencia, entender la relación entre los factores y el salario del CEO.

n = 500

p = 4

#### (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or failure, price charged for the product, marketing budget, competition price, and ten other variables.

Tipo de Problema: Clasificación.

Interés Principal: Predicción, determinar si el nuevo producto será un éxito o un fracaso.

n = 20

p = 15

#### (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in the world stock markets. Hence we collect weekly data for all of 2012. For each week we record the % change in the USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

Tipo de Problema: Regresión.

Interés Principal: Predicción, determinar el % de cambio en la tasa de cambio USD/Euro en función de los cambios semanales en los mercados bursátiles mundiales.

n = 52

p = 4

### 5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

Ventajas de un enfoque muy flexible:

- Captura de Relaciones Complejas: Un enfoque flexible, como el uso de un modelo complejo como una red neuronal profunda o un árbol de decisiones con muchos nodos, puede capturar relaciones intrincadas y no lineales en los datos.

- Mayor Precisión: En situaciones donde la relación subyacente entre los predictores y la respuesta es compleja, un modelo flexible puede proporcionar una mayor precisión al ajustarse más estrechamente a los datos de entrenamiento.

- Adaptabilidad: Los modelos flexibles pueden adaptarse bien a patrones diversos y cambiantes en los datos, lo que los hace adecuados para sistemas dinámicos o en evolución.

Podría preferirse este tipo de enfoques cuando la relación entre los predictores y la respuesta es compleja y no lineal, cuando contamos con conjuntos de datos grandes y diversos, o en análisis exploratorios donde el objetivo principal es la predicción en lugar de la interpretación.

En cambio, podría preferirse un enfoque menos flexibles cuando la interpretabilidad es crucial, como en campos donde las explicaciones del modelo son esenciales, en escenarios con datos limitados (evita overfitting), o si los recursos computacionales son limitados.

### 6. Describe the diﬀerences between a parametric and a non-parametric statistical learning approach. What are the advantages of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its disadvantages?

Los modelos paramétricos y no paramétricos difieren en la cantidad de suposiciones que hacen sobre la forma de la relación funcional entre los predictores y la respuesta. Mientras que los modelos paramétricos asumen una forma específica para la función (por ejemplo, regresiones lineales), lo que implica estimar un número limitado de parámetros, los modelos no paramétricos no hacen suposiciones sobre la forma de la función y pueden adaptarse a patrones más complejos, lo que resulta en la estimación de un mayor número de elementos.

La elección entre un enfoque paramétrico y no paramétrico depende de varios factores. Los modelos paramétricos son preferidos cuando las suposiciones estructuradas son válidas y se dispone de datos limitados. Tienen la ventaja de ser más eficientes computacionalmente y más fácilmente interpretables. Por otro lado, los modelos no paramétricos son ideales cuando se busca mayor flexibilidad y no se conocen las relaciones funcionales a priori.

En términos de regresión o clasificación, un enfoque flexible tiene la ventaja de reducir el sesgo al aproximar problemas de la vida real, lo que puede traducirse en un menor error. Sin embargo, este enfoque también presenta la desventaja de aumentar la varianza, lo que significa que los resultados pueden variar considerablemente al estimarse con otro conjunto de datos. Si el verdadero patrón no es lineal y hay un número suficiente de observaciones, un enfoque flexible tiende a producir mejores resultados. Por el contrario, si asumimos que el patrón es lineal, un método menos flexible, como la regresión lineal, puede ser preferible al tener menos sesgo.

### 7. The table below provides a training data set containing six observations, three predictors, and one qualitative response variable.

| Obs. | X1  | X2  | X3  |  Y   |
|------|----|----|----|-------|
|  1   |  0 |  3 |  0 |  Red  |
|  2   |  2 |  0 |  0 |  Red  |
|  3   |  0 |  1 |  3 |  Red  |
|  4   |  0 |  1 |  2 | Green |
|  5   | -1 |  0 |  1 | Green |
|  6   |  1 |  1 |  1 |  Red  |

### Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

#### (a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

| **Observación** | **Distancia Euclidiana** |
|------------------|---------------------------|
| 1                | 3                         |
| 2                | 2                         |
| 3                | \(\sqrt{10}\)             |
| 4                | \(\sqrt{5}\)              |
| 5                | \(\sqrt{2}\)              |
| 6                | \(\sqrt{3}\)              |

#### (b) What is our prediction with K = 1? Why?

La predicción es Y = Green porque la **Observación 4** tiene la distancia Euclidiana más corta (1).

#### (c) What is our prediction with K = 3? Why?

La predicción es Y = Red porque 2 de sus 3 vecinos más cercanos tienen la clase Red.

#### (d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to be large or small? Why?

Si la frontera de decisión de Bayes es altamente no lineal, se espera que un valor óptimo para K sea pequeño. Esto se debe a que un valor pequeño de K permite al algoritmo capturar patrones más locales y no dependerá tanto de la estructura global de los datos. Un valor grande de K suavizaría demasiado la frontera de decisión y podría perder los detalles no lineales presentes en los datos.

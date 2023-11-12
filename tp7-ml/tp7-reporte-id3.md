### A. Resultados sobre la evaluación sobre tennis.csv

    'outlook': {
        'overcast': 'yes',
        'rainy': {
            'windy': {
                False: 'yes', 
                True: 'no'
            }
        },
        'sunny': {
            'humidity': {
                'high': 'no', 
                'normal': 'yes'
            }
        }
    }

### B. Información sobre las estrategias para datos de tipo real

Los árboles de decisión son versátiles y pueden manejar tanto datos categóricos como datos numéricos de tipo real. Estas son algunas de las estrategias más comunes para datos de tipo real:

- **Bifurcación basada en umbrales numéricos:** Los nodos del árbol de decisión pueden realizar bifurcaciones basadas en umbrales numéricos para manejar variables continuas. Por ejemplo, un nodo podría dividir los datos en dos ramas según si una característica numérica es mayor o igual a un cierto umbral.

- **Criterios de impureza:** Los árboles de decisión utilizan criterios de impureza (como la ganancia de información, índice de Gini o error cuadrático medio) para decidir cómo dividir los datos en cada nodo. Estos criterios se aplican tanto a variables categóricas como a variables numéricas.

- **Podas y ajustes:** Para evitar overfitting, se pueden utilizar estrategias de poda y ajuste en los árboles de decisión. La poda controla la profundidad del árbol, y se pueden aplicar umbrales para determinar cuándo dejar de dividir un nodo en función de la impureza o la ganancia de información.

- **Algoritmos específicos:** Algunos algoritmos de árboles de decisión, como CART (Classification and Regression Trees), están diseñados para manejar variables numéricas de manera eficiente. Estos algoritmos pueden determinar automáticamente los umbrales óptimos para la división de variables numéricas.

- **Transformación de variables:** Antes de construir el árbol, se pueden aplicar transformaciones a variables numéricas, como discretización o normalización, para mejorar la capacidad del árbol para capturar patrones.

import pandas as pd
import numpy as np

# Función para calcular la entropía de un conjunto de datos
def entropy(data):
    if len(data) == 0:
        return 0
    p = data.value_counts(normalize=True)
    return -np.sum(p * np.log2(p))

# Función para calcular la ganancia de información de un atributo
def information_gain(data, attribute_name, class_name):
    total_entropy = entropy(data[class_name])
    values = data[attribute_name].unique()
    weighted_entropy = 0

    for value in values:
        subset = data[data[attribute_name] == value]
        weighted_entropy += len(subset) / len(data) * entropy(subset[class_name])

    return total_entropy - weighted_entropy

# Función para encontrar la mayoría de la clase en un conjunto de datos
def plurality_value(data, class_name):
    return data[class_name].value_counts().idxmax()

# Función para construir un árbol de decisión basado en Ganancia de Información
def decision_tree_learning(examples, attributes, parent_examples, class_name):
    if len(examples) == 0:
        return plurality_value(parent_examples, class_name)
    elif len(examples[class_name].unique()) == 1:
        return examples[class_name].iloc[0]
    elif len(attributes) == 0:
        return plurality_value(examples, class_name)
    else:
        best_attribute = max(attributes, key=lambda a: information_gain(examples, a, class_name))
        tree = {best_attribute: {}}
        attributes.remove(best_attribute)
        for value in examples[best_attribute].unique():
            subset = examples[examples[best_attribute] == value]
            subtree = decision_tree_learning(subset, attributes.copy(), examples, class_name)
            tree[best_attribute][value] = subtree
        return tree

# Cargar tus datos desde un archivo CSV
data = pd.read_csv("https://raw.githubusercontent.com/sjwhitworth/golearn/master/examples/datasets/tennis.csv")

# Especifica el nombre de la columna de la clase y la columna de los atributos
class_name = "play"
attribute_names = ["outlook", "temp", "humidity", "windy"]

# Construir el árbol de decisión
decision_tree = decision_tree_learning(data, attribute_names, data, class_name)

# Mostrar el árbol
import pprint
pprint.pprint(decision_tree)

# Detección de casos de bullying

### Código del proyecto: BULL

### Integrantes: Francisco Devaux y Bautista Frigolé

### Descripción

Nuestro proyecto de inteligencia artificial se enfoca en la detección y predicción de casos de bullying utilizando técnicas de machine learning. El objetivo principal de esta iniciativa es desarrollar un modelo capaz de identificar situaciones de acoso entre estudiantes, con el fin de prevenir y abordar este grave problema que afecta a jóvenes en todo el mundo. Para lograr esto, hemos empleado el [dataset](https://www.kaggle.com/datasets/leomartinelli/bullying-in-schools) del Global School-Based Student Health Survey (GSHS) realizado en Argentina en 2018, que proporciona una amplia gama de información relevante sobre la salud y el comportamiento de los jóvenes.

El Global School-Based Student Health Survey (GSHS) es una encuesta basada en escuelas que utiliza un cuestionario autoadministrado para recopilar datos sobre el comportamiento de salud de los jóvenes y los factores protectores relacionados con las principales causas de morbilidad y mortalidad. En la edición realizada en Argentina en 2018, participaron un total de 56,981 estudiantes.

El dataset cuenta con 18 variables entre las cuales se destacan:

- Suffered bullying in past 12 months
- Age
- Sex
- Felt lonely
- Close friends amount
- Miss school with no permission
- Parents understand problems
- Were underweight
- Were obese

### Objetivo

El objetivo fundamental de nuestro proyecto es desarrollar un modelo de machine learning que permita predecir situaciones de bullying en base a las demás variables. Al utilizar técnicas avanzadas de análisis de datos y aprendizaje automático, aspiramos a identificar patrones y relaciones ocultas en los datos que nos permitan anticipar casos de bullying, proporcionando así una herramienta efectiva para la prevención y el apoyo a los estudiantes afectados.

### Justificación

Al desarrollar un modelo de predicción sólido, se puede brindar una herramienta valiosa para la detección temprana y la prevención del bullying mediante encuestas en grandes cantidades de estudiantes, algo que no podría ser posible sin el uso de técnicas de inteligencia artificial, avisando de estos posibles casos de bullying a profesionales para que tomen cartas en el asunto. Este modelo podría contribuir al bienestar de los estudiantes y a la creación de un entorno escolar más seguro y saludable.

### Estado del arte

Se ha llevado a cabo una búsqueda de proyectos con características similares a nuestro objetivo de desarrollo. La mayoría de los documentos encontrados se centran en la clasificación a partir de texto, a diferencia de los datos normalizados que tenemos previsto utilizar. A continuación, se presentan algunos de los artículos destacados:

- [**"Cyber Bullying and Machine Learning: A Survey"**](https://zenodo.org/record/4249341/files/01%20Paper%2001102001%20IJCSIS%20Camera%20Ready%20pp1-8.pdf)  
   - Autores: Ibtihaj Alanazi, Jim Alves-Foss (2020)

- [**"Identifying depression in the National Health and Nutrition Examination Survey data using a deep learning algorithm"**](https://www.sciencedirect.com/science/article/abs/pii/S0165032719304410)  
   - Autores: Jihoon Oh, Kyongsik Yun, Uri Maoz, Tae-Suk Kim, Jeong-Ho Chae (2019)

Adicionalmente, en relación al dataset con el que planeamos trabajar, se han llevado a cabo proyectos similares que están disponibles en la plataforma Kaggle. Algunos de ellos incluyen:

- [**"Bullying in Schools - EDA"**](https://www.kaggle.com/code/anzarwani2/bullying-in-schools-eda)  
   - Autor: Anzarwani2 (2023)

- [**"Bullying in School Prediction"**](https://www.kaggle.com/code/sridharstreaks/bullying-in-school-prediction)  
   - Autor: Sridhar Streaks (2023)
   - Se utilizan árboles de decisión, obteniendo 76.29% de accuracy.

- [**"Bullying in Schools"**](https://www.kaggle.com/code/ashokrajuyadav/bullying-in-schools)
   - Autor: Ashok Raju Onteru (2023)
   - Se utilizan distintos algoritmos de random forest con oversampling (XGboost y SKLEARN), obteniendo 70.28% y 77.37% de accuracy, respectivamente.

### Métricas

Para evaluar la eficacia del modelo de detección de bullying, utilizaremos un conjunto de métricas clásicas en problemas de clasificación. Estas métricas proporcionarán una visión más completa del rendimiento del modelo, complementando la tasa de observaciones correctamente detectadas. Aquí están las métricas que consideraremos:

1. **Precisión (Precision):**
   - Descripción: La precisión mide la proporción de instancias positivas correctamente clasificadas respecto a todas las instancias clasificadas como positivas.
   - Fórmula: Precision = TP / (TP + FP)
   - Interpretación: Proporción de casos positivos predichos correctamente entre todos los casos predichos como positivos.

2. **Recall (Sensibilidad o Tasa de Verdaderos Positivos):**
   - Descripción: El recall mide la proporción de instancias positivas correctamente clasificadas respecto a todas las instancias que son realmente positivas.
   - Fórmula: Recall = TP / (TP + FN)
   - Interpretación: Proporción de casos positivos predichos correctamente entre todos los casos reales positivos.

3. **F1-Score:**
   - Descripción: El F1-score es la media armónica de la precisión y el recall, proporcionando un equilibrio entre ambas métricas.
   - Fórmula: F1 = 2 * (Precision * Recall) / (Precision + Recall)
   - Interpretación: Combina precisión y recall en una única métrica, ideal para problemas con desequilibrio de clases.

4. **Exactitud (Accuracy):**
   - Descripción: La exactitud mide la proporción de instancias correctamente clasificadas, independientemente de la clase.
   - Fórmula: Accuracy = (TP + TN) / (TP + TN + FP + FN)
   - Interpretación: Proporción de todas las predicciones correctas.

5. **Especificidad (Tasa de Verdaderos Negativos):**
   - Descripción: La especificidad mide la proporción de instancias negativas correctamente clasificadas respecto a todas las instancias realmente negativas.
   - Fórmula: Especificidad = TN / (TN + FP)
   - Interpretación: Proporción de casos negativos predichos correctamente entre todos los casos reales negativos.

6. **Curva ROC y Área bajo la Curva (AUC-ROC):**
   - Descripción: La curva ROC representa la tasa de verdaderos positivos frente a la tasa de falsos positivos para diferentes umbrales de decisión. El AUC-ROC mide la capacidad del modelo para distinguir entre clases.
   - Interpretación: Un AUC-ROC cercano a 1 indica un buen rendimiento del modelo.

Es importante evaluar estas métricas en conjunto, ya que proporcionan información valiosa sobre diferentes aspectos del rendimiento del modelo. Dependiendo de los requisitos específicos y las implicaciones prácticas del problema, algunas métricas pueden tener más relevancia que otras.


### Listado de actividades a realizar

1. Recopilación y Limpieza de Datos [4 días]:
   - Realizar limpieza de datos para eliminar valores nulos o inconsistentes.

2. Análisis Exploratorio de Datos [6 días]:
   - Explorar las estadísticas descriptivas de las variables seleccionadas.
   - Visualizar gráficamente las distribuciones y relaciones entre las variables.

3. Ingeniería de Características [5 días]:
   - Identificar y crear características relevantes para el modelo, como variables categóricas y numéricas.
   - Normalizar o estandarizar datos si es necesario.

4. División del Conjunto de Datos [2 días]:
   - Selección de la técnica para dividir el conjunto de datos en conjuntos de entrenamiento, validación y prueba.
   - Solucionar problemas de desequilibrio de clases en el conjunto de datos.

5. Selección del Modelo de Machine Learning [6 días]:
   - Investigar y seleccionar un modelo de machine learning adecuado para la predicción de bullying, como clasificadores (Random Forest y otro modelo como por ej. SVM).
   - En vista de lo hecho en Kaggle, probar los algoritmos ya planteados en los notebooks. En particular, Árbol de decisión y Random Forests (XGboost y SKLEARN).

6. Entrenamiento del Modelo [2 días]:
   - Implementar y entrenar el modelo seleccionado con el conjunto de entrenamiento.

7. Validación y Ajuste Fino [3 días]:
   - Evaluar el modelo en el conjunto de validación.
   - Realizar ajustes y mejoras según los resultados de la validación cruzada.

8. Evaluación del Modelo [1 días]:
   - Probar el modelo final en el conjunto de prueba para evaluar su rendimiento.
   - Calcular métricas como precisión, sensibilidad, especificidad y la tasa de observaciones correctamente detectadas.
   - Realizar una comparación entre los 2 modelos elegidos que, en principio, serían Random Forest y SVM. Considerando que ambos modelos pueden tener features distintas.
   - Realizar un test de hipótesis entre los 2 modelos elegidos.

9. Interpretación de Resultados [2 días]:
   - Analizar las predicciones del modelo para identificar patrones y características clave asociadas con casos de bullying.

10. Escritura de informe final [12 días].

### Cronograma estimado de actividades (gantt)

![Facultad(2)](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/9d85c431-ba1c-4618-b2b5-a450254aa268)

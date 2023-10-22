### 2. A partir del archivo arbolado-mendoza-dataset-train.csv responder las siguientes preguntas:
#### ¿Cual es la distribución de las clase inclinacion_peligrosa?

La distribución de las clases es la siguiente:

![DistribucionClasesInclinacionPeligrosa](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/fd7676c9-86a1-4b4b-be1e-5c0a6b46facf)

Como se puede observar, la gran mayoría de los árboles no tienen inclinación peligrosa.

#### ¿Se puede considerar alguna sección más peligrosa que otra?

![ProporcionInclinacionPeligrosaPorSección](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/602b9de3-84d4-492f-b82c-1a4dee0756e0)

Como se puede ver en el gráfico, sí hay secciones que cuentan con mayor proporción de árboles con inclinación peligrosa.

#### ¿Se puede considerar alguna especie más peligrosa que otra?

![ProporcionInclinacionPeligrosaPorEspecie](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/a0399e5f-9e7b-45ea-87b4-3d2e7ed63ce0)

Sí, en base al gráfico presentado, se puede observar que la especie Algarrobo es la que cuenta con mayor proporción de árboles con inclinación peligrosa, siendo levemente mayor a 0.5.


### 3. A partir del archivo arbolado-mendoza-dataset-train.csv,
#### b. Histograma de frecuencia para la variable circ_tronco_cm. 

![HistrogramaCircunferenciaTronco](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/619f0434-8b34-4130-a21b-80d61e4eeb25)

#### c. Histograma de frecuencia para la variable circ_tronco_cm pero separando por la clase de la variable inclinación_peligrosa.

![HistrogramaCircunferenciaTroncoInclinacionPeligrosa](https://github.com/bautifrigole/ia-uncuyo-2023/assets/64384449/ad064200-5d47-4eaf-9bc6-4b0411a5708e)

#### d. Criterios de corte para cada categoría de circ_tronco_cm_cat [bajo, medio, alto, muy alto]:

Se tomaron los cortes de la siguiente manera: (0, 60, 180, 250, Inf).

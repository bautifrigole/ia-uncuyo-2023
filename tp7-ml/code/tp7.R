library(dplyr)
library(ggplot2)

# Carga los datos desde el archivo CSV
dataframe <- read.csv("data/arbolado-mza-dataset.csv")
dataframe

# Define el tamaño del conjunto de validación (en este caso, 20%)
validation_size <- 0.20

# Divide el conjunto de datos en entrenamiento y validación de manera aleatoria
set.seed(123)  # Establece una semilla para reproducibilidad
validation_data <- dataframe %>% sample_frac(validation_size)
train_data <- anti_join(dataframe, validation_data)  # Datos de entrenamiento

train_data <- read.csv("data/arbolado-mendoza-dataset-train.csv")

# Guarda los conjuntos de datos en archivos CSV separados
write.csv(validation_data, "data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(train_data, "data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)

train_data<-train_data %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))

# 2
# a. Distribución de las clases de inclinación peligrosa
ggplot(train_data, aes(x = inclinacion_peligrosa)) +
  geom_bar() +
  labs(title = "Distribución de Clases de Inclinación Peligrosa", x = "Clase", y = "Frecuencia")

# b. Sección más peligrosa
ggplot(train_data, aes(x = seccion, fill = factor(inclinacion_peligrosa))) +
  geom_bar(position = "fill") +
  labs(title = "Proporción de Inclinación Peligrosa por Sección", x = "Sección", y = "Porcentaje") +
  scale_fill_manual(values = c("no" = "green", "si" = "red"))

# c. Especie más peligrosa
ggplot(train_data, aes(x = especie, fill = factor(inclinacion_peligrosa))) +
  geom_bar(position = "fill") +
  labs(title = "Proporción de Inclinación Peligrosa por Especie", x = "Especie", y = "Porcentaje") +
  scale_fill_manual(values = c("no" = "green", "si" = "red")) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))

# 3
# b. Generar un histograma para la variable circ_tronco_cm con diferentes números de bins
par(mfrow=c(2,2))  # Crear una cuadrícula de 2x2 para mostrar varios histogramas

hist(train_data$circ_tronco_cm, main="Histograma (5 bins)", xlab="circ_tronco_cm", breaks=5)
hist(train_data$circ_tronco_cm, main="Histograma (10 bins)", xlab="circ_tronco_cm", breaks=10)
hist(train_data$circ_tronco_cm, main="Histograma (20 bins)", xlab="circ_tronco_cm", breaks=20)
hist(train_data$circ_tronco_cm, main="Histograma (30 bins)", xlab="circ_tronco_cm", breaks=30)

# c. Histograma de circ_tronco_cm separado por inclinación_peligrosa
ggplot(train_data, aes(x = circ_tronco_cm, fill = inclinacion_peligrosa)) +
  geom_histogram(binwidth = 10, position = "identity") +
  labs(title = "Histograma de circ_tronco_cm separado por inclinación_peligrosa", 
       x = "circ_tronco_cm",
       y = "Frecuencia") +
  scale_fill_manual(values = c("si" = "red", "no" = "green")) +
  theme_minimal()

# Restaura la configuración de múltiples gráficos a la configuración original
par(mfrow = c(1, 1))

# d. Crear la nueva variable categórica circ_tronco_cm_cat
train_data <- train_data %>% 
  mutate(circ_tronco_cm_cat = cut(circ_tronco_cm, 
                                  breaks = c(0, 60, 180, 250, Inf),
                                  labels = c("bajo", "medio", "alto", "muy alto"),
                                  include.lowest = TRUE))

# Guardar el nuevo dataframe en un archivo CSV
write_csv(train_data, "./data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")


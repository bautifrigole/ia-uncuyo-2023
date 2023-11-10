library(dplyr)
library(ggplot2)
library(readr)
library(rpart)

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


train_data <- read.csv("data/arbolado-mendoza-dataset-circ_tronco_cm-train.csv")

# 4
# a. Función para agregar una nueva columna con valores aleatorios entre 0 y 1
generate_random_prediction_prob <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  data$prediction_prob <- runif(nrow(data))
  return(data)
}

# Llama a la función y proporciona el data.frame como argumento
train_data <- generate_random_prediction_prob(train_data)

# b. Definir la función random_classifier
random_classifier <- function(data) {
  # Generar la nueva columna prediction_class basada en la columna prediction_prob
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)
  return(data)
}

# Cargar el archivo "arbolado-mendoza-dataset-validation.csv" como un data.frame
validation_data <- read.csv("data/arbolado-mendoza-dataset-validation.csv")

# Llama a la función y proporciona el data.frame como argumento
validation_data <- generate_random_prediction_prob(validation_data)

# c. Aplicar la función random_classifier al data.frame de validación
validation_data <- random_classifier(validation_data)

# Ver el data.frame resultante con la nueva columna prediction_class
head(validation_data)

#d.
calculate_confusion_matrix <- function(actual, predicted) {
  TP <- sum(actual == 1 & predicted == 1)
  TN <- sum(actual == 0 & predicted == 0)
  FP <- sum(actual == 0 & predicted == 1)
  FN <- sum(actual == 1 & predicted == 0)
  
  confusion_matrix <- data.frame(TP = TP, TN = TN, FP = FP, FN = FN)
  
  return(confusion_matrix)
}

# Utilizar la función para calcular la matriz de confusión
confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

# Ver la matriz de confusión
print(confusion_matrix)


# 5
# a. Definir la función biggerclass_classifier
biggerclass_classifier <- function(data) {
  # Calcular la clase mayoritaria
  majority_class <- ifelse(sum(data$inclinacion_peligrosa == "si") > sum(data$inclinacion_peligrosa == "no"), 1, 0)
  
  # Asignar la clase mayoritaria a la columna prediction_class
  data$prediction_class <- majority_class
  
  return(data)
}

# b. Aplicar la función biggerclass_classifier al data.frame validation_data
validation_data <- biggerclass_classifier(validation_data)

# Utilizar la función para calcular la matriz de confusión
confusion_matrix <- calculate_confusion_matrix(validation_data$inclinacion_peligrosa, validation_data$prediction_class)

# Ver la matriz de confusión
print(confusion_matrix)


# 6
# Función para calcular Accuracy
calculate_accuracy <- function(confusion_matrix) {
  accuracy <- (confusion_matrix$TP + confusion_matrix$TN) / (confusion_matrix$TP + confusion_matrix$TN + confusion_matrix$FP + confusion_matrix$FN)
  return(accuracy)
}

# Función para calcular Precision
calculate_precision <- function(confusion_matrix) {
  precision <- confusion_matrix$TP / (confusion_matrix$TP + confusion_matrix$FP)
  return(precision)
}

# Función para calcular Sensitivity
calculate_sensitivity <- function(confusion_matrix) {
  sensitivity <- confusion_matrix$TP / (confusion_matrix$TP + confusion_matrix$FN)
  return(sensitivity)
}

# Función para calcular Specificity
calculate_specificity <- function(confusion_matrix) {
  specificity <- confusion_matrix$TN / (confusion_matrix$TN + confusion_matrix$FP)
  return(specificity)
}

# Función para calcular Negative Predicted Value
calculate_negative_predicted <- function(confusion_matrix) {
  negative_predicted <- confusion_matrix$TN / (confusion_matrix$TN + confusion_matrix$FN)
  return(negative_predicted)
}

# Ejemplo de uso:
# Supongamos que tienes una matriz de confusión llamada "confusion_matrix"
accuracy_value <- calculate_accuracy(confusion_matrix)
precision_value <- calculate_precision(confusion_matrix)
sensitivity_value <- calculate_sensitivity(confusion_matrix)
specificity_value <- calculate_specificity(confusion_matrix)
negative_predicted_value <- calculate_negative_predicted(confusion_matrix)

# Imprimir los valores de las métricas
cat("Accuracy:", accuracy_value, "\n")
cat("Precision:", precision_value, "\n")
cat("Sensitivity:", sensitivity_value, "\n")
cat("Specificity:", specificity_value, "\n")
cat("Negative Predicted Value:", specificity_value, "\n")


# 7
# a. Definir la función create_folds
create_folds <- function(df, k) {
  shuffled_data = df[sample(1:nrow(df)), ] 
  
  # Calculate the number of rows in each fold
  fold_size <- nrow(shuffled_data) %/% k
  fold_sizes <- rep(fold_size, k)
  
  # Distribute the remaining rows if any
  remaining_rows <- nrow(shuffled_data) %% k
  fold_sizes[1:remaining_rows] <- fold_sizes[1:remaining_rows] + 1
  
  # Split the shuffled dataframe into k folds
  folds <- split(shuffled_data, rep(1:k, fold_sizes))
  
  # Convert the folds to a list
  fold_list <- as.list(folds)
  
  return(fold_list)
}

# b. Definir la función cross_validation
cross_validation <- function(df, k) {
  folded_data <- create_folds(df, k)
  
  result <- data.frame(
    Accuracy = numeric(),
    Precision = numeric(),
    Sensitivity = numeric(),
    Specificity = numeric()
  )
  for (i in 1:length(folded_data)) {
    validation_set <- folded_data[[i]]
    trainings_sets <- folded_data[-i]
    
    training_df <- do.call(rbind, trainings_sets)
    train_formula <- formula(inclinacion_peligrosa ~ altura + diametro_tronco)
    tree_model <- rpart(train_formula, data = training_df)
    p <- predict(tree_model, validation_set, type = "class")
    
    true_labels <- validation_set$inclinacion_peligrosa
    confusion_matrix <- calculate_confusion_matrix(true_labels, p)
    
    accuracy <- calculate_accuracy(confusion_matrix)
    precision <- calculate_precision(confusion_matrix)
    sensitivity <- calculate_sensitivity(confusion_matrix)
    specificity <- calculate_specificity(confusion_matrix)
    
    row_metrics <- data.frame(
      Accuracy = accuracy,
      Precision = precision,
      Sensitivity = sensitivity,
      Specificity = specificity
    )
    
    result <- rbind(result, row_metrics)
  }
  
  print(result)
  return(result)
}

data <- read_csv("./data/arbolado-mendoza-dataset-validation.csv")
data$inclinacion_peligrosa = as.factor(data$inclinacion_peligrosa)

result_df <- cross_validation(data, 10)
result_df

readr::write_csv(result_df, "./metrics.csv")
data <- read.csv("./metrics.csv", header = TRUE)
means <- colMeans(data, na.rm = TRUE)

# Calcular la desviación estándar de cada columna
std_dev <- apply(data, 2, sd, na.rm = TRUE)

# Crear un nuevo dataframe con las medias y desviaciones estándar
summary_data <- data.frame(
  Metrica = c("Accuracy", "Precision", "Sensitivity", "Specificity"),
  Media = means,
  Desviacion_Estandar = std_dev
)

summary_data
write.csv(summary_data, "resultados.csv", row.names = FALSE)

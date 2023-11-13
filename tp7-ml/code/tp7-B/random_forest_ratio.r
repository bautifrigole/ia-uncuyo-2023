library(randomForest)
library(dplyr)
library(readr)

# Leer los datos de entrenamiento
data_train <- readr::read_csv("./data/arbolado-mza-dataset.csv",
                              col_types = cols(
                                id = col_integer(),
                                especie = col_character(),
                                ultima_modificacion = col_character(),
                                altura = col_character(),
                                circ_tronco_cm = col_double(),
                                diametro_tronco = col_character(),
                                long = col_double(),
                                lat = col_double(),
                                seccion = col_integer(),
                                nombre_seccion = col_character(),
                                area_seccion = col_double(),
                                inclinacion_peligrosa = col_integer()
                              ))

# Eliminar las columnas no deseadas
data_train <- data_train %>% select(-id, -nombre_seccion, -area_seccion, -diametro_tronco, -altura)

# Leer los datos de prueba
data_test <- readr::read_csv("./data/arbolado-mza-dataset-test.csv", col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))

# Eliminar las columnas no deseadas en los datos de prueba
data_test <- data_test %>% select(-nombre_seccion, -area_seccion, diametro_tronco, -altura)

# Separar los datos en dos grupos según el valor de inclinacion_peligrosa
data_no_inclinacion <- data_train %>% filter(inclinacion_peligrosa == 0)
data_si_inclinacion <- data_train %>% filter(inclinacion_peligrosa == 1)

# Definir diferentes ratios de muestreo (puedes ajustar estos valores según tus necesidades)
ratios <- c(1, 2, 3)  # Ejemplo de ratios 1:1, 1:2, y 1:3

# Crear una lista para almacenar los modelos y predicciones
models <- list()
predictions <- list()

# Iterar a través de los diferentes ratios
for (ratio in ratios) {
  # Seleccionar una cantidad de ejemplos de la clase inclinación peligrosa igual a 0
  sampled_data_no_inclinacion <- data_no_inclinacion %>%
    sample_n(size = ratio * nrow(data_si_inclinacion), replace = TRUE)
  
  # Combinar los dos grupos seleccionados para crear un conjunto de entrenamiento balanceado
  balanced_trainset <- bind_rows(sampled_data_no_inclinacion, data_si_inclinacion)
  
  # Convertir la variable objetivo en factor
  balanced_trainset$inclinacion_peligrosa <- as.factor(balanced_trainset$inclinacion_peligrosa)
  
  # Entrenar el modelo con los datos balanceados
  model <- randomForest(inclinacion_peligrosa ~ ., data = balanced_trainset, ntree = 500)
  model
  
  # Realizar predicciones en los datos de prueba
  preds_tree_probs <- predict(model, data_test, type = 'prob')
  
  # Almacenar el modelo y las predicciones
  models[[as.character(ratio)]] <- model
  predictions[[as.character(ratio)]] <- preds_tree_probs[, 2]  # Usar la probabilidad de la clase positiva
}

models

# Calcular el promedio de las predicciones o usar un enfoque de voto ponderado
# Puedes ajustar esta parte según tu enfoque de combinación de resultados
average_predictions <- rowMeans(do.call(cbind, predictions))

# Convertir las probabilidades promedio en clases
combined_preds_tree <- ifelse(average_predictions >= 0.5, 1, 0)

# Crear un marco de datos de resultados y guardarlos en un archivo CSV
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = combined_preds_tree)
readr::write_csv(submission, "./envios/arbolado-mza-dataset-envio-randomForest-ratio.csv")
head(submission)

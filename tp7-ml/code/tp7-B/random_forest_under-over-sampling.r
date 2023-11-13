library(randomForest)
library(ROSE)
library(dplyr)
library(readr)

# Lee los datos de entrenamiento
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

# Elimina las columnas no deseadas
data_train <- data_train %>% select(-id, -nombre_seccion, -area_seccion, -diametro_tronco, -altura)

# Realiza el undersampling en la clase inclinación peligrosa
undersampled_data <- ovun.sample(inclinacion_peligrosa ~ ., data = data_train, method = "under", N = 2 * sum(data_train$inclinacion_peligrosa))

# Realiza el oversampling en la clase inclinación peligrosa (duplica los casos)
oversampled_data <- ovun.sample(inclinacion_peligrosa ~ ., data = data_train, method = "over", p = 0.5, seed = 123)

# Combina los datos undersampled y oversampled
combined_data <- bind_rows(undersampled_data$data, oversampled_data$data)

# Convierte la variable objetivo en factor
combined_data$inclinacion_peligrosa <- as.factor(combined_data$inclinacion_peligrosa)

# Entrena el modelo usando Random Forest
model <- randomForest(inclinacion_peligrosa ~ ., data = combined_data, ntree = 500, mtry = 1)
model

# Lee los datos de prueba
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

# Elimina las columnas no deseadas en los datos de prueba
data_test <- data_test %>% select(-nombre_seccion, -area_seccion, diametro_tronco, -altura)

# Realiza predicciones en los datos de prueba
preds_tree_probs <- predict(model, data_test, type = 'prob')

# Convierte las probabilidades en clases
preds_tree <- ifelse(preds_tree_probs[, 2] >= 0.5, 1, 0)

# Crea un marco de datos de resultados y guárdalos en un archivo CSV
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_tree)
readr::write_csv(submission, "./envios/arbolado-mza-dataset-envio-randomForest-over-under.csv")
head(submission)

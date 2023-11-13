library(randomForest)
library(caret)
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
data_train <- data_train %>% select(-id, -nombre_seccion, -area_seccion, -diametro_tronco)

# Divide los datos en características (X) y variable objetivo (y)
X <- data_train %>% select(-inclinacion_peligrosa)
y <- data_train$inclinacion_peligrosa

# Crear un objeto de control para la validación cruzada
ctrl <- trainControl(method = "cv", number = 30)  # Número de folds (cambia según tus necesidades)

# Entrenar el modelo usando randomForest con validación cruzada
set.seed(123)  # Fija una semilla para reproducibilidad
model <- train(X, y, method = "rf", trControl = ctrl)
print(model)

# Realizar predicciones en los datos de prueba
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

# Realizar predicciones en los datos de prueba
preds_tree <- predict(model, newdata = data_test)

# Crear un marco de datos de resultados y guardarlos en un archivo CSV
submission <- data.frame(id = data_test$id, inclinacion_peligrosa = preds_tree)
readr::write_csv(submission, "./envios/arbolado-mza-dataset-envio-randomForest-kfolds.csv")
head(submission)

suppressMessages(library(rpart))
suppressMessages(library(caret))
suppressMessages(library(readr))
suppressMessages(library(dplyr))

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

data_test <-  readr::read_csv("./data/arbolado-mza-dataset-test.csv",col_types = cols(
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

data_train<-data_train %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))
data_train$inclinacion_peligrosa <-as.factor(data_train$inclinacion_peligrosa)

train_formula<-formula(inclinacion_peligrosa~altura+circ_tronco_cm+lat+long+seccion+especie)
tree_model_3<-rpart(train_formula,data=data_train)

preds_tree_probs=predict(tree_model_3,data_test,type='prob')
head(preds_tree_probs)

preds_tree=ifelse(preds_tree_probs[,2] >=0.5,1,0)
head(preds_tree)

submission<-data.frame(id=data_test$id,inclinacion_peligrosa=preds_tree)
readr::write_csv(submission,"./envios/arbolado-mza-dataset-envio-ejemplo-rpart.csv")
head(submission)

set.seed(100) # para que sea un ejemplo reproducible
data_validation_index<-sample(nrow(data_train),nrow(data_train)*0.1)
data_validation<-data_train[data_validation_index,]
data_train<-data_train[-data_validation_index,]

train_formula<-formula(inclinacion_peligrosa~altura+circ_tronco_cm+lat+long+seccion+especie)
tree_model_4<-rpart(train_formula,data=data_train)

preds_tree_probs=predict(tree_model_4,data_validation,type='prob')
preds_tree=ifelse(preds_tree_probs[,2] >=0.5,'si','no')
resultados_validation<-data.frame(inclinacion_peligrosa=preds_tree)

confusionMatrix(resultados_validation$inclinacion_peligrosa,data_validation$inclinacion_peligrosa)

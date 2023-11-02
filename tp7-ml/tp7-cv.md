### A. El código (en un bloque de código) de las funciones create_folds() y cross_validation()

```R
create_folds <- function(data, k) {
  n <- nrow(data)
  fold_size <- n %/% k
  remainder <- n %% k
  
  folds <- list()
  start_idx <- 1
  
  for (i in 1:k) {
    end_idx <- start_idx + fold_size - 1
    if (i <= remainder) {
      end_idx <- end_idx + 1
    }
    fold_indices <- start_idx:end_idx
    folds[[paste0("Fold", i)]] <- fold_indices
    start_idx <- end_idx + 1
  }
  
  return(folds)
}
```

```R
cross_validation <- function(df, k, tformula) {
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
    
    tree_model <- rpart(tformula, data = training_df)
    p <- predict(tree_model, validation_set, type="class")
    
    true_labels <- validation_set$inclinacion_peligrosa
    crow <- confusion_matrix_imp(data = p, reference = true_labels) %>% get_metrics()
    result[nrow(result) + 1, ] <- crow
  }
  
  return(result)
}
```

### B. Una tabla con los resultados (media y desviación estándar de las métricas seleccionadas) de aplicar el clasificador un árbol de decisión en los distintos conjuntos

| Metrica      | Media                | Desviacion_Estandar    |
|--------------|----------------------|------------------------|
| Accuracy     | 0.814652719637625    | 0.252637105254083      |
| Precision    | 0.916666666666667    | 0.288675134594813      |
| Sensitivity  | 0.814652719637625    | 0.252637105254083      |
| Specificity  | NA                   | NA                     |

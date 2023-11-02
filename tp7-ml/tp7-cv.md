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

### B. Una tabla con los resultados (media y desviación estándar de las métricas seleccionadas) de aplicar el clasificador un árbol de decisión en los distintos conjuntos


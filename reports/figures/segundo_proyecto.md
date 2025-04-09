# Segundo Proyecto: Feature Engineering y Modelado

## 1. Objetivo del proyecto

Predecir la variable `QUANTITY` (cantidad de productos vendidos) usando variables contextuales del producto y de la venta, como precio unitario, ingresos, mes, entre otras. El objetivo práctico es anticipar la demanda y mejorar la gestión de inventario y ventas.

## 2. Descripción del dataset

El dataset proviene de un sistema contable ERP y contiene información de ventas como:
- PRODUCTID
- PRICE_UNITARIO
- INGRESO_TOTAL
- FECHA (usada para extraer MES, AÑO, DÍA)
- CATEGORÍA DE PRODUCTO

## 3. Ingeniería de variables (Feature Engineering)

Se aplicaron técnicas como:
- Conversión de fechas a variables numéricas (`MES`, `AÑO`, `DÍA`)
- One-hot encoding para `PRODUCTID` y `CATEGORÍA`
- Normalización y escalado
- Creación de variables relevantes como `INGRESO_TOTAL`

## 4. Modelado y evaluación

Se entrenaron y evaluaron los siguientes modelos:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

### Métricas utilizadas:
- MAE (Error Absoluto Medio)
- RMSE (Raíz del Error Cuadrático Medio)
- R² (Coeficiente de determinación)

### Resultados generales:

| Modelo            | MAE      | RMSE     | R²       |
|-------------------|----------|----------|----------|
| Decision Tree     | 0.003633 | 0.035504 | 0.998702 |
| Random Forest     | 0.015141 | 0.035856 | 0.998676 |
| Gradient Boosting | 0.091658 | 0.118688 | 0.985493 |
| Linear Regression | 0.548454 | 0.697852 | 0.498493 |

## 5. Interpretabilidad

Se generaron gráficos de:
- Importancia de variables (Feature Importance)
- Árbol de decisión
- SHAP values
- Partial Dependence Plot (PDP)

## 6. Conclusión

En este proyecto se desarrolló un modelo de regresión para predecir la cantidad de productos vendidos (`QUANTITY`). Los modelos basados en árboles (especialmente el Árbol de Decisión) ofrecieron una excelente capacidad predictiva, superando a la regresión lineal con una diferencia clara en precisión. Esta solución permitirá a la empresa anticipar la demanda y optimizar su gestión de inventarios, logística y estrategia comercial.

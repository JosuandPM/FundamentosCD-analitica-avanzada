# Proyecto: Predicción de Ventas e Inventario

Este repositorio contiene el desarrollo de un proyecto de ciencia de datos enfocado en la **predicción de ventas e inventario** utilizando datos extraídos de un sistema contable ERP (SAP). Los datos fueron descargados desde Kaggle y simulan información real de una empresa de bicicletas.

## Objetivo del Proyecto

Analizar, limpiar, transformar y organizar los datos de ventas, productos, órdenes y categorías para construir una base sólida que permita la creación de modelos predictivos que estimen la demanda (cantidad) y optimicen el manejo de inventario.

---

## Estructura del Repositorio

### 1. **[EDA.ipynb](./EDA.ipynb)**
Contiene el Análisis Exploratorio de Datos:
- Estadísticas descriptivas.
- Visualizaciones iniciales.
- Detección de valores faltantes y outliers.
- Evaluación de qué archivos y columnas se utilizarán en la etapa de modelado.

### 2. **[Data_Wrangling.ipynb](./Data_Wrangling.ipynb)**
Contiene el proceso de limpieza y transformación:
- Eliminación de columnas irrelevantes.
- Tratamiento de valores nulos y duplicados.
- Normalización de nombres de columnas.
- Creación de las tablas finales `fct_ventas` y `dim_productos`.
- Exportación de archivos .csv limpios y consolidados.

---

## Archivos de Datos Utilizados (Carpeta: `../datasets/raw/`)

- `SalesOrderItems.csv`
- `Products.csv`
- `ProductTexts.csv`
- `ProductCategories.csv`

---

## Archivos Exportados (Carpeta: `../datasets/clean/`)

- `clean_orden_ventas_item.csv`
- `clean_productos.csv`
- `clean_texto_productos.csv`
- `clean_texto_categoria_productos.csv`
- `fct_ventas.csv`
- `dim_productos.csv`

---

## Requisitos

- Python 3.9+
- Pandas
- Matplotlib
- Jupyter Notebook

---

## Autor

**Josue Paredes**
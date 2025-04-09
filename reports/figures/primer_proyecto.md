
# Proyecto 2 - Parte 1: EDA y Data Wrangling

## Objetivo

Explorar, limpiar y preparar los datos de ventas de un sistema ERP para la posterior etapa de Feature Engineering y Modelado, enfocándose en la predicción de `QUANTITY`, la cantidad de productos vendidos.

## 1. Análisis Exploratorio de Datos (EDA)

Se trabajó con cuatro archivos principales:

- `SalesOrderItems.csv`: ítems vendidos por orden.
- `SalesOrders.csv`: información general de cada orden.
- `Products.csv`: información del producto.
- `ProductCategoryText.csv` y `ProductText.csv`: descripciones de categorías y productos.

### Principales hallazgos:
- La variable `QUANTITY` presenta una distribución con outliers que fueron detectados con boxplots.
- `PRICE_UNITARIO` y `INGRESO_TOTAL` son las variables más correlacionadas con la cantidad vendida.
- Las variables `ANIO`, `MES`, `DIA_SEMANA` fueron derivadas correctamente desde fechas para análisis temporal.
- Se descartaron columnas con valores nulos altos o sin aporte al modelo, como `WIDTH`, `HEIGHT`, `GROSSAMOUNT`, `NOTEID`, etc.

Se generaron visualizaciones de:
- Cantidades vendidas por día y por mes.
- Tendencias de ventas por categoría y producto.
- Relación entre precio unitario e ingreso total.

## 2. Limpieza y Preparación (Data Wrangling)

### Procesos realizados:
- Conversión de fechas (`DELIVERYDATE`) al tipo datetime.
- Conversión de `QUANTITY` a tipo entero.
- Imputación de valores nulos con la media en columnas como `NETAMOUNT` y `PRICE_UNITARIO`.
- Eliminación de columnas no numéricas o irrelevantes.
- Estandarización y renombrado de variables para consistencia.

### Tablas creadas:
- `clean_orden_ventas_item`
- `clean_productos`
- `clean_texto_productos`
- `clean_texto_categoria_productos`
- `fct_ventas`: unión de órdenes y productos
- `dim_productos`: unión de producto + descripción + categoría

## Conclusión

Gracias al EDA se identificaron las variables más relevantes para el modelado, y a través del proceso de limpieza se logró construir un conjunto de datos estructurado y consistente. Esto permitió exportar versiones limpias para continuar con la etapa de Feature Engineering en el segundo notebook.

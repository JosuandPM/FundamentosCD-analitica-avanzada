
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

try:
    from xgboost import XGBRegressor
    xgb_available = True
except ImportError:
    xgb_available = False

def dividir_datos(df, target='QUANTITY', test_size=0.2, random_state=42):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def entrenar_modelos(X_train, y_train):
    modelos = {
        'LinearRegression': LinearRegression(),
        'DecisionTree': DecisionTreeRegressor(random_state=42),
        'RandomForest': RandomForestRegressor(random_state=42),
        'GradientBoosting': GradientBoostingRegressor(random_state=42)
    }
    if xgb_available:
        modelos['XGBoost'] = XGBRegressor(random_state=42)

    entrenados = {}
    for nombre, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        entrenados[nombre] = modelo
    return entrenados

def evaluar_modelos(modelos, X_test, y_test):
    resultados = []
    for nombre, modelo in modelos.items():
        pred = modelo.predict(X_test)
        mae = mean_absolute_error(y_test, pred)
        rmse = mean_squared_error(y_test, pred, squared=False)
        r2 = r2_score(y_test, pred)
        resultados.append({
            'Modelo': nombre,
            'MAE': mae,
            'RMSE': rmse,
            'R2': r2
        })
    return pd.DataFrame(resultados).sort_values(by='RMSE')

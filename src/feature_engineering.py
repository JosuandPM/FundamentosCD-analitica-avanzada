
import pandas as pd

def agregar_variables_temporales(df, fecha_col='DELIVERYDATE'):
    df[fecha_col] = pd.to_datetime(df[fecha_col])
    df['ANIO'] = df[fecha_col].dt.year
    df['MES'] = df[fecha_col].dt.month
    df['DIA'] = df[fecha_col].dt.day
    df['DIA_SEMANA'] = df[fecha_col].dt.day_name()
    return df

def agregar_ingreso_total(df, cantidad_col='QUANTITY', precio_col='PRICE_UNITARIO'):
    df['INGRESO_TOTAL'] = df[cantidad_col] * df[precio_col]
    return df

def crear_lag_features(df, grupo='PRODUCTID', variable='QUANTITY', lags=[1, 7]):
    df = df.sort_values(by=[grupo, 'DELIVERYDATE'])
    for lag in lags:
        df[f'{variable}_LAG_{lag}'] = df.groupby(grupo)[variable].shift(lag)
    return df

def crear_rolling_means(df, grupo='PRODUCTID', variable='QUANTITY', ventanas=[3, 7]):
    df = df.sort_values(by=[grupo, 'DELIVERYDATE'])
    for ventana in ventanas:
        df[f'{variable}_ROLLING_{ventana}'] = (
            df.groupby(grupo)[variable]
              .rolling(window=ventana)
              .mean()
              .reset_index(level=0, drop=True)
        )
    return df

def codificar_categoricas(df, columnas):
    for col in columnas:
        df[col] = df[col].astype(str)
    df_codificado = pd.get_dummies(df, columns=columnas, drop_first=True)
    return df_codificado

def escalar_columnas(df, columnas):
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

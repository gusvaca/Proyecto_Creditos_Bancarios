"""Funciones utilitarias para el proyecto de predicción de créditos."""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def cargar_datos(ruta):
    """Carga el dataset de créditos bancarios.
    
    Args:
        ruta (str): Ruta del archivo CSV
        
    Returns:
        pd.DataFrame: DataFrame con los datos cargados
    """
    return pd.read_csv(ruta)


def limpiar_datos(df):
    """Limpia el dataset eliminando valores faltantes.
    
    Args:
        df (pd.DataFrame): DataFrame a limpiar
        
    Returns:
        pd.DataFrame: DataFrame limpio
    """
    return df.dropna()


def escalar_datos(X_train, X_test):
    """Escala los datos usando StandardScaler.
    
    Args:
        X_train: Features de entrenamiento
        X_test: Features de prueba
        
    Returns:
        tuple: (X_train_scaled, X_test_scaled)
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled

"""Módulo para construcción y evaluación del modelo Random Forest."""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


class ModeloCreditos:
    """Clase para manejar el modelo de predicción de créditos."""
    
    def __init__(self, random_state=42):
        """Inicializa el modelo.
        
        Args:
            random_state (int): Semilla para reproducibilidad
        """
        self.modelo = RandomForestClassifier(random_state=random_state)
        self.metricas = {}
    
    def entrenar(self, X_train, y_train):
        """Entrena el modelo.
        
        Args:
            X_train: Features de entrenamiento
            y_train: Target de entrenamiento
        """
        self.modelo.fit(X_train, y_train)
    
    def predecir(self, X_test):
        """Realiza predicciones.
        
        Args:
            X_test: Features para predicción
            
        Returns:
            np.array: Predicciones
        """
        return self.modelo.predict(X_test)
    
    def evaluar(self, y_test, y_pred):
        """Evalúa el modelo con métricas.
        
        Args:
            y_test: Target real
            y_pred: Predicciones del modelo
        """
        self.metricas = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1_score': f1_score(y_test, y_pred, average='weighted')
        }
        return self.metricas
    
    def importancia_features(self, feature_names):
        """Obtiene la importancia de las features.
        
        Args:
            feature_names: Nombres de las features
            
        Returns:
            dict: Diccionario con importancia de features
        """
        return dict(zip(feature_names, self.modelo.feature_importances_))

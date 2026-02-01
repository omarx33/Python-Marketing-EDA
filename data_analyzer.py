"""
Clase DataAnalyzer para análisis exploratorio de datos
Proyecto: Bank Marketing EDA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Tuple

class DataAnalyzer:
    """
    Clase para encapsular funciones de análisis exploratorio de datos
    """
    
    def __init__(self, dataframe: pd.DataFrame):
        """
        Inicializa el analizador con un DataFrame
        
        Args:
            dataframe: DataFrame de pandas a analizar
        """
        self.df = dataframe
        self.numeric_cols = None
        self.categorical_cols = None
        self._classify_variables()
    
    def _classify_variables(self):
        """
        Clasifica las variables en numéricas y categóricas
        """
        self.numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
    
    def get_basic_info(self) -> Dict:
        """
        Retorna información básica del dataset
        
        Returns:
            Diccionario con información del dataset
        """
        info = {
            'shape': self.df.shape,
            'columns': self.df.columns.tolist(),
            'dtypes': self.df.dtypes.to_dict(),
            'null_counts': self.df.isnull().sum().to_dict(),
            'total_nulls': self.df.isnull().sum().sum()
        }
        return info
    
    def get_variable_classification(self) -> Dict:
        """
        Retorna la clasificación de variables
        
        Returns:
            Diccionario con variables numéricas y categóricas
        """
        return {
            'numeric': self.numeric_cols,
            'categorical': self.categorical_cols,
            'n_numeric': len(self.numeric_cols),
            'n_categorical': len(self.categorical_cols)
        }
    
    def get_descriptive_stats(self, variables: List[str] = None) -> pd.DataFrame:
        """
        Calcula estadísticas descriptivas
        
        Args:
            variables: Lista de variables a analizar (None = todas las numéricas)
            
        Returns:
            DataFrame con estadísticas descriptivas
        """
        if variables is None:
            variables = self.numeric_cols
        
        return self.df[variables].describe()
    
    def get_missing_values_analysis(self) -> pd.DataFrame:
        """
        Analiza valores faltantes
        
        Returns:
            DataFrame con conteo y porcentaje de valores faltantes
        """
        missing = pd.DataFrame({
            'Columna': self.df.columns,
            'Valores_Nulos': self.df.isnull().sum().values,
            'Porcentaje': (self.df.isnull().sum().values / len(self.df) * 100).round(2)
        })
        return missing.sort_values('Valores_Nulos', ascending=False)
    
    def get_value_counts(self, column: str, normalize: bool = False) -> pd.Series:
        """
        Obtiene conteo de valores para una columna categórica
        
        Args:
            column: Nombre de la columna
            normalize: Si True, retorna proporciones
            
        Returns:
            Serie con conteos o proporciones
        """
        return self.df[column].value_counts(normalize=normalize)
    
    def plot_numeric_distribution(self, column: str, ax=None):
        """
        Grafica la distribución de una variable numérica
        
        Args:
            column: Nombre de la columna numérica
            ax: Eje de matplotlib (opcional)
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(10, 6))
        
        sns.histplot(data=self.df, x=column, kde=True, ax=ax)
        ax.set_title(f'Distribución de {column}', fontsize=14, fontweight='bold')
        ax.set_xlabel(column, fontsize=12)
        ax.set_ylabel('Frecuencia', fontsize=12)
        
        # Agregar líneas de media y mediana
        mean_val = self.df[column].mean()
        median_val = self.df[column].median()
        ax.axvline(mean_val, color='red', linestyle='--', label=f'Media: {mean_val:.2f}')
        ax.axvline(median_val, color='green', linestyle='--', label=f'Mediana: {median_val:.2f}')
        ax.legend()
        
        return ax
    
    def plot_categorical_distribution(self, column: str, ax=None):
        """
        Grafica la distribución de una variable categórica
        
        Args:
            column: Nombre de la columna categórica
            ax: Eje de matplotlib (opcional)
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))
        
        value_counts = self.df[column].value_counts()
        sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax, palette='viridis')
        ax.set_title(f'Distribución de {column}', fontsize=14, fontweight='bold')
        ax.set_xlabel(column, fontsize=12)
        ax.set_ylabel('Frecuencia', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        
        # Agregar valores en las barras
        for i, v in enumerate(value_counts.values):
            ax.text(i, v + max(value_counts.values)*0.01, str(v), 
                   ha='center', va='bottom', fontsize=10)
        
        return ax
    
    def plot_bivariate_numeric_categorical(self, numeric_col: str, categorical_col: str, ax=None):
        """
        Grafica relación entre variable numérica y categórica
        
        Args:
            numeric_col: Variable numérica
            categorical_col: Variable categórica
            ax: Eje de matplotlib (opcional)
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))
        
        sns.boxplot(data=self.df, x=categorical_col, y=numeric_col, ax=ax, palette='Set2')
        ax.set_title(f'{numeric_col} vs {categorical_col}', fontsize=14, fontweight='bold')
        ax.set_xlabel(categorical_col, fontsize=12)
        ax.set_ylabel(numeric_col, fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        
        return ax
    
    def plot_categorical_crosstab(self, col1: str, col2: str, ax=None):
        """
        Grafica tabla cruzada entre dos variables categóricas
        
        Args:
            col1: Primera variable categórica
            col2: Segunda variable categórica
            ax: Eje de matplotlib (opcional)
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 8))
        
        crosstab = pd.crosstab(self.df[col1], self.df[col2])
        sns.heatmap(crosstab, annot=True, fmt='d', cmap='YlOrRd', ax=ax)
        ax.set_title(f'Relación: {col1} vs {col2}', fontsize=14, fontweight='bold')
        
        return ax
    
    def get_correlation_matrix(self, variables: List[str] = None) -> pd.DataFrame:
        """
        Calcula matriz de correlación
        
        Args:
            variables: Lista de variables (None = todas las numéricas)
            
        Returns:
            DataFrame con matriz de correlación
        """
        if variables is None:
            variables = self.numeric_cols
        
        return self.df[variables].corr()
    
    def plot_correlation_heatmap(self, variables: List[str] = None, ax=None):
        """
        Grafica heatmap de correlación
        
        Args:
            variables: Lista de variables (None = todas las numéricas)
            ax: Eje de matplotlib (opcional)
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(14, 10))
        
        corr_matrix = self.get_correlation_matrix(variables)
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, ax=ax, square=True, linewidths=1)
        ax.set_title('Matriz de Correlación', fontsize=16, fontweight='bold')
        
        return ax
    
    def get_summary_statistics(self, column: str) -> Dict:
        """
        Obtiene estadísticas de resumen para una columna
        
        Args:
            column: Nombre de la columna
            
        Returns:
            Diccionario con estadísticas
        """
        if column in self.numeric_cols:
            stats = {
                'Media': self.df[column].mean(),
                'Mediana': self.df[column].median(),
                'Moda': self.df[column].mode()[0] if len(self.df[column].mode()) > 0 else None,
                'Desviación Estándar': self.df[column].std(),
                'Mínimo': self.df[column].min(),
                'Máximo': self.df[column].max(),
                'Q1': self.df[column].quantile(0.25),
                'Q3': self.df[column].quantile(0.75)
            }
        else:
            stats = {
                'Valores únicos': self.df[column].nunique(),
                'Moda': self.df[column].mode()[0] if len(self.df[column].mode()) > 0 else None,
                'Frecuencia moda': self.df[column].value_counts().iloc[0]
            }
        
        return stats

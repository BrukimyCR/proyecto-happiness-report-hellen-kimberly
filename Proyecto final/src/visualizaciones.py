import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Configuración de color ---
color_rosado = '#ffb6c1'  # Light Pink

# --- Funciones de gráficos ---
def graficar_barras(df, columna, titulo, xlabel, ylabel):
    plt.figure(figsize=(12,6))
    plt.bar(df['Country'], df[columna], color=color_rosado)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def graficar_scatter(df, x_col, y_col, titulo, xlabel, ylabel):
    plt.figure(figsize=(8,6))
    plt.scatter(df[x_col], df[y_col], alpha=0.7, color=color_rosado, edgecolors='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def graficar_heatmap(df):
    # Selecciona solo columnas numéricas para evitar errores
    df_numerico = df.select_dtypes(include='number')
    
    plt.figure(figsize=(10,8))
    correlation = df_numerico.corr()
    sns.heatmap(correlation, annot=True, cmap='pink', fmt=".2f")  # Usamos la paleta "pink"
    plt.title('Mapa de calor de correlaciones', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

def graficar_histograma(df, columna, titulo, xlabel, ylabel):
    plt.figure(figsize=(8,6))
    plt.hist(df[columna], bins=15, color=color_rosado, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

# --- Unificar nombres de columnas ---
def estandarizar_columnas(df):
    df = df.rename(columns={
        'Economy (GDP per Capita)': 'GDP per capita',
        'Family': 'Social support',
        'Happiness Score': 'Score',
        'Happiness.Rank': 'Happiness Rank',  # por si en 2015-2016 viene con punto
    })
    return df








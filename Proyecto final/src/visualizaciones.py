import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_barras(df, columna, titulo, xlabel, ylabel):
    plt.figure(figsize=(12,6))
    plt.bar(df['Country'], df[columna], color='skyblue')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def graficar_scatter(df, x_col, y_col, titulo, xlabel, ylabel):
    plt.figure(figsize=(8,6))
    plt.scatter(df[x_col], df[y_col], alpha=0.7)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()

def graficar_heatmap(df):
    plt.figure(figsize=(10,8))
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Mapa de calor de correlaciones')
    plt.tight_layout()
    plt.show()

def graficar_histograma(df, columna, titulo, xlabel, ylabel):
    plt.figure(figsize=(8,6))
    plt.hist(df[columna], bins=15, color='skyblue', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()

def cargar_y_unir_data(data_folder):
    archivos = ['2015.csv', '2016.csv', '2017.csv', '2018.csv', '2019.csv']
    dfs = []
    for archivo in archivos:
        ruta = os.path.join(data_folder, archivo)
        df = pd.read_csv(ruta)
        año = int(archivo.split('.')[0])
        df['Year'] = año
        dfs.append(df)
    df_combinado = pd.concat(dfs, ignore_index=True)
    return df_combinado

if __name__ == "__main__":
    carpeta_data = 'Proyecto final/data'
    df = cargar_y_unir_data(carpeta_data)
    print("Datos cargados y combinados. Columnas:", df.columns)

    # Agrupar por país y obtener promedio solo columnas numéricas
    df_promedio = df.groupby('Country').mean(numeric_only=True).reset_index()

    # Top 15 países por PIB
    df_top15 = df_promedio.sort_values(by='Economy (GDP per Capita)', ascending=False).head(15)
    graficar_barras(df_top15, 'Economy (GDP per Capita)', 'Promedio PIB per cápita (2015-2019) - Top 15 países', 'País', 'PIB per cápita')

    # Top 15 países por soporte social
    df_top15_soporte = df_promedio.sort_values(by='Social support', ascending=False).head(15)
    graficar_barras(df_top15_soporte, 'Social support', 'Promedio Soporte Social (2015-2019) - Top 15 países', 'País', 'Soporte Social')

    # Scatter plot PIB vs felicidad (usa todos los datos)
    graficar_scatter(df, 'Economy (GDP per Capita)', 'Happiness Score', 'Relación entre PIB y Felicidad (2015-2019)', 'PIB per cápita', 'Puntaje de Felicidad')



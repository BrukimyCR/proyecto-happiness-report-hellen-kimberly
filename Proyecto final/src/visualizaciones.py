import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cargar_y_combinar_csv(ruta_carpeta):
    archivos = ['2015.csv', '2016.csv', '2017.csv', '2018.csv', '2019.csv']
    lista_df = []
    for archivo in archivos:
        ruta = os.path.join(ruta_carpeta, archivo)
        df = pd.read_csv(ruta)
        df['Year'] = archivo.split('.')[0]  # Agregar columna de año
        lista_df.append(df)
    df_combinado = pd.concat(lista_df, ignore_index=True)
    return df_combinado

def graficar_barras(df, columna, titulo, xlabel, ylabel):
    plt.figure(figsize=(12,6))
    # Agrupar por país y hacer promedio para esa columna
    promedio = df.groupby('Country or region')[columna].mean().sort_values(ascending=False).head(15)
    plt.bar(promedio.index, promedio.values, color='skyblue')
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
    correlation = df.select_dtypes(include='number').corr()
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

if __name__ == "__main__":
    ruta_data = 'Proyecto final/data'
    df = cargar_y_combinar_csv(ruta_data)
    print("Datos cargados y combinados. Columnas:", df.columns)

    # Cambia los nombres de las columnas si es necesario, porque pueden variar según el año
    # Por ejemplo, 'GDP per capita' podría estar como 'GDP per capita' o 'GDP per capita (PPP)'

    # Revisa los nombres exactos de las columnas con:
    # print(df.columns)

    # Gráfico barras PIB per cápita promedio (ajusta nombre columna si da error)
    graficar_barras(df, 'GDP per capita', 'Promedio PIB per cápita (2015-2019) - Top 15 países', 'País', 'PIB per cápita')

    # Gráfico barras soporte social promedio
    graficar_barras(df, 'Social support', 'Promedio Soporte Social (2015-2019) - Top 15 países', 'País', 'Soporte Social')

    # Scatter plot PIB vs felicidad (ajusta nombre de columnas si es necesario)
    graficar_scatter(df, 'GDP per capita', 'Happiness score', 'Relación entre PIB y Felicidad (2015-2019)', 'PIB per cápita', 'Puntaje de felicidad')

    # Histograma puntaje felicidad
    graficar_histograma(df, 'Happiness score', 'Distribución del Puntaje de Felicidad (2015-2019)', 'Puntaje de felicidad', 'Frecuencia')

    # Heatmap de correlaciones
    graficar_heatmap(df)


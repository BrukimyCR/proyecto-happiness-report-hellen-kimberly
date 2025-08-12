import pandas as pd
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

if __name__ == "__main__":
    ruta_csv = '../data/world-happiness-report.csv'
    df = pd.read_csv(ruta_csv)

    # Gráfico de barras del PIB per cápita
    graficar_barras(df, 'GDP per capita', 'PIB per cápita por País', 'País', 'PIB per cápita')

    # Gráfico de barras del soporte social
    graficar_barras(df, 'Social support', 'Soporte Social por País', 'País', 'Soporte Social')

    # Scatter plot PIB vs felicidad
    graficar_scatter(df, 'GDP per capita', 'Happiness Score', 'Relación entre PIB y Felicidad', 'PIB per cápita', 'Puntaje de felicidad')

    # Histograma del puntaje de felicidad
    graficar_histograma(df, 'Happiness Score', 'Distribución del Puntaje de Felicidad', 'Puntaje de felicidad', 'Frecuencia')

    # Heatmap de correlaciones
    graficar_heatmap(df)


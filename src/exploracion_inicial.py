import pandas as pd

def cargar_dataset(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        print("✅ Dataset cargado correctamente.\n")
        return df
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado. Verifica el nombre o la ruta.")
    except pd.errors.ParserError:
        print("❌ Error: Formato incorrecto o archivo corrupto.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

def exploracion_basica(df):
    print("🔍 Dimensiones del dataset (filas, columnas):")
    print(df.shape)

    print("\n🧩 Tipos de datos por columna:")
    print(df.dtypes)

    print("\n📊 Estadísticas descriptivas:")
    print(df.describe(include='all'))

    print("\n🕵️‍♂️ Conteo de valores nulos por columna:")
    print(df.isnull().sum())

    print("\n📝 Primeras 5 filas del dataset:")
    print(df.head())

if __name__ == "__main__":
    ruta_csv = "data/world-happiness-report.csv"
    datos = cargar_dataset(ruta_csv)
    if datos is not None:
        exploracion_basica(datos)



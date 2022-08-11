import pandas as pd
import pathlib

rutaFileCsv = "https://raw.githubusercontent.com/luisguillermomolero/MisionTIC2022_2/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv"

def listaPeliculas(rutaFileCsv: str) -> str:
    ruta = pathlib.Path(rutaFileCsv)
    extension = ruta.suffix
    #if rutaFileCsv.split('.')[-1] == "csv?raw=true":
    if extension == ".csv":
        try:
            peliculas = pd.read_csv(rutaFileCsv)
            peliculas_pais_idioma_ingresos = peliculas[["Country", "Language", "Gross Earnings"]]
            peliculas_index_pais_idioma = peliculas_pais_idioma_ingresos.pivot_table(index=["Country", "Language"])
            return peliculas_index_pais_idioma.head(10)
        except:
            print("Error al leer el archivo de datos.")
    else:
        print("Extensión inválida.")   
           
print(listaPeliculas(rutaFileCsv))            






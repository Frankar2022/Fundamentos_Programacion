import pandas as pd
import pathlib 

rutaFileCsv = "https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true"

def listaPeliculas(rutaFileCsv: str) -> str:
    ruta = pathlib.Path(rutaFileCsv)
    extension = ruta.suffix
    if  extension == ".csv?raw=true":
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






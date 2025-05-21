import os


def listar_archivos(ruta):
    #lista los archivos de un directorio o carpeta
    lista_archivos = os.listdir(ruta)
    return lista_archivos

print(os.getcwd())

ruta_absoluta = os.getcwd()
#La ruta relativa como estamos en la misma carpeta pasarle un (.)
ruta_relativa = "."
archivos = listar_archivos(ruta_absoluta)
print(f"Archivos en la ruta {archivos}:")


archivos2 = listar_archivos(ruta_relativa)
print(f"Archivos en la ruta {archivos2}:")


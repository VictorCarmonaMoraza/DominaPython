# Ciclos -> Iterar objetos(for,while)
# Ciclos dentro de ciclos -> ciclos anidados
# Funcion zip() -> retornar un conjunto de tuplas

lista_nombres = ['Juan', 'Pedro', 'Maria', 'Ana']
lista_edades = [25, 30, 22, 28]

 #Uniremos las listas en un objeto iterable
datos_zip = zip(lista_nombres, lista_edades)
#Veremos una lista de 4 tuplas
print(list(datos_zip))

print("===================================")

lista_nombres2 = [ 'Pedro', 'Maria', 'Ana']
lista_edades2 = [25, 30, 22, 28]

 #Uniremos las listas en un objeto iterable
datos_zip2 = zip(lista_nombres2, lista_edades2)
#Como tenemos solo 3 nombres y 4 edadees, solo se uniran 3 tuplas
print(list(datos_zip2))

print("===============CICLO FO====================")
for nombre, edad in zip(lista_nombres, lista_edades):
    print(f"Nombre: {nombre}, Edad: {edad}")
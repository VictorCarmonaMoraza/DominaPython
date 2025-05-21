print("cadena de texto")

variable =1
print(f'Variable {variable}')

#elementos separados por coma. Por defecto sep=None es este pero no hace falta poner
print("elementos","separados", "por", "comas")

#Agregamos el separador de (.)
print("elementos","separados", "por", "comas", sep=".")

#Agregamos sepradores de escape, para imprimir cada uno en una linea diferente
print("elementos","separados", "por", "comas", sep="\n")

#Como queremos que termine lo que estamos imprimiendo
print("Primero", end=".")
print("Segundo")


#Donde se va a escrinbir lo que vamos a impirmir
with open("print_ejemplo.txt", "w") as archivo:
    print("Hola XXXXXXXXX", file=archivo)
    

#Limpiar buffer interno
import time

print("INICIO", end="...", flush=True)
time.sleep(2)
print("FIN")

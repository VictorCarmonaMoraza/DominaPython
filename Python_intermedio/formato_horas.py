# Uso de las fechas
# * Creacion de reportes
# * Bases de datos
# * Tareas programadas


#Importamos la libreria datetime
from datetime import datetime

#Obtenemos la fecha y hora actual
ahora = datetime.now()

#Imprimimos la fecha y hora actual con su tipo
print(ahora, type(ahora))

#Convertir un objeto datetime a un string
fecha_str = ahora.strftime("%Y-%m-%d")
print(fecha_str, type(fecha_str))

#Ver la hora en formato 24 horas
hora_str = ahora.strftime("%H:%M:%S")
print(f"Formato 24 horas {hora_str}, {type(hora_str)}")

#formato de 12 horas
hora_str_12 = ahora.strftime("%I:%M:%S %p")
print(f"Formato 12 horas {hora_str_12}, {type(hora_str_12)}")

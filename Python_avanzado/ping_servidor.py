#Hacer ping a un servidor significa enviar una señal a un servidor para verificar su disponibilidad y tiempo de respuesta. En Python, esto se puede hacer utilizando la biblioteca `subprocess` para ejecutar el comando `ping` del sistema operativo. A continuación, se presenta un ejemplo de cómo implementar esta funcionalidad en Python:
# se hace ping a servidores o dominios

import os

def hacer_ping(hostname):
    respuesta = os.system(f"ping {hostname}")
    #etorna cero si el ping fue exitoso
    if respuesta == 0:
        print(f"{hostname} está activo")
    else:
        print(f"{hostname} no está activo")


hacer_ping("linkedion.com")
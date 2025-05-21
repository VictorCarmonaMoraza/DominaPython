#Son para escribir instrucciones hacia el SO

import subprocess

nombre_bash = "bash_example.sh"
contenido = ""

with open(nombre_bash, mode="rb") as archivo_bash:
    contenido = archivo_bash.read()
    contenido_str = contenido.decode('utf-8')
    
print(f'Contenido del archivo : {contenido_str}')
subprocess.call(contenido_str, shell=True)
#Debemos instalar la libreria psutil que es para conoecer los recuros de nuestra maquie
# pip install psutil
import psutil


def recursos_usados_cpu():
    print(f"--------------Obtener nucleos CPU-----------------")
    #Cantidad de nucleos de la maquina
    #True serian nucleos Logicos
    #False serian nucleos Fisicos
    nucleos = psutil.cpu_count(logical=False)
    print(f"Nucleos de la maquina: {nucleos}")
    
    print(f"--------------Carga Promedia de la CPU-----------------")
    #Obtener la carga promedia de la cpu
    carga_cpu = psutil.getloadavg()
    print(f"Carga CPU: {carga_cpu}")
    
    print(f"--------------Obtenemos  CPU-----------------")
    #Obtenemos el porcentaje de uso de la CPU
    uso_cpu = psutil.cpu_percent(interval=5,percpu=True)
    print(f"Porcentaje de uso de la CPU: {uso_cpu}")
    

recursos_usados_cpu()
    
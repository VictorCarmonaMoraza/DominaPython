#necesario la instalacion: pip install phonenumbers
import phonenumbers

def validar_tefefono(telefono_str, codigo_pais=None):
    try:
        telefono = phonenumbers.parse(telefono_str, codigo_pais)
        return phonenumbers.is_valid_number(telefono)
    except Exception as e:
        print(e)
        return False

#Numeracion de Colombia
valido = validar_tefefono("+573001002030")
valido2 = validar_tefefono("3001002030", "CO")
print("Telefono valido:",valido)
print("Telefono valido:",valido2)
try:
    print("Texto con formato {}".format())
except Exception as e:
    raise Exception("Ha ocurrido un error")


try:
    print("Texto con formato {}".format())
except Exception as e:
    e.add_note("Error en la funcion format")
    print(e.__notes__)


import os
from PIL import Image


def abrir_imagen(ruta_img):
    imagen = Image.open(ruta_img)
    imagen.show()

ruta_relativa ="sandia.png"
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)

#Para utilizar pillow siempre debemos utilizar la ruta absoluta
abrir_imagen(ruta_absoluta)


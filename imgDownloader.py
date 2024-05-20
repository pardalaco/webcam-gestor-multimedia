import requests
import os
from datetime import datetime
import time
import numpy as np


def descargar_imagen(url):
    try:
        # Definir un User-Agent personalizado
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Realizar la solicitud GET a la URL con el User-Agent personalizado
        respuesta = requests.get(url, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # print("Imagen descargada exitosamente")

            return respuesta.content
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

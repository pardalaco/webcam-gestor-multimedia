import requests
import os
from datetime import datetime
import time

def descargar_imagen(url, directorio_destino):
    try:
        # Definir un User-Agent personalizado
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Realizar la solicitud GET a la URL con el User-Agent personalizado
        respuesta = requests.get(url, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:

            
            # Guardar la imagen en un archivo
            ahora = datetime.now()
            fecha_actual = ahora.strftime("%Y-%m-%d")
            hora_actual = ahora.strftime("%H_%M_%S")
            nombre_archivo = f"menejador_alcoi_{fecha_actual}_{hora_actual}.jpg"
            ruta_guardado = os.path.join(directorio_destino, nombre_archivo)
            with open(ruta_guardado, 'wb') as archivo:
                archivo.write(respuesta.content)
            print("La imagen se ha descargado correctamente como:", nombre_archivo)
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

def suspender_programa(minutos):
    # Convertir minutos a segundos
    segundos = minutos * 60
    # Suspender el programa durante el tiempo especificado
    time.sleep(segundos)
    print(f"El programa ha sido suspendido durante {minutos} minutos y ha vuelto a reanudarse.")

# URL de la página web
url_pagina = 'https://www.acifalcoi.com/webcam/menejador.jpg'

# Directorio donde se guardarán las imágenes descargadas
directorio_destino = './img'

# Llamar a la función para descargar la imagen
while(True):
    descargar_imagen(url_pagina, directorio_destino)
    suspender_programa(1.2)

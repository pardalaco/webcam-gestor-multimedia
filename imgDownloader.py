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
            # Llamar a la función para guardar la imagen
            guardar_imagen(respuesta.content, directorio_destino)
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

def guardar_imagen(imagen, directorio_destino):
    try:
        # Obtener la fecha y hora actual
        ahora = datetime.now()
        fecha_actual = ahora.strftime("%Y-%m-%d")
        hora_actual = ahora.strftime("%H_%M_%S")
        
        # Crear el nombre de archivo usando la fecha y hora actual
        nombre_archivo = f"menejador_alcoi_{fecha_actual}_{hora_actual}.jpg"
        
        # Crear la ruta completa para guardar la imagen
        ruta_guardado = os.path.join(directorio_destino, fecha_actual, nombre_archivo)
        
        # Crear la carpeta del día si no existe
        if not os.path.exists(os.path.join(directorio_destino, fecha_actual)):
            os.makedirs(os.path.join(directorio_destino, fecha_actual))
        
        # Guardar la imagen en un archivo
        with open(ruta_guardado, 'wb') as archivo:
            archivo.write(imagen)
        
        print(nombre_archivo+" > "+ruta_guardado)
    except Exception as e:
        print("Ocurrió un error al guardar la imagen:", str(e))

def suspender_programa(minutos):
    # Convertir minutos a segundos
    segundos = minutos * 60
    # Suspender el programa durante el tiempo especificado
    time.sleep(segundos)

def main():
    print("Starting imgDownloader.py")

    # URL de la página web
    url_pagina = 'https://www.acifalcoi.com/webcam/menejador.jpg'

    # Directorio donde se guardarán las imágenes descargadas
    directorio_destino = './img'

    try:
        while True:
            descargar_imagen(url_pagina, directorio_destino)
            suspender_programa(1.05)
    except KeyboardInterrupt:
        print("\nCtrl + C detectado. Deteniendo el programa imgDownloader.py.")

if __name__ == "__main__":
    main()

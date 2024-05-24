import requests
import os
from datetime import datetime
import time
import imgDownloader as dw
import configs

# Función la cual se le pasa una imagen y un directorio, y guarda la imagen con el formato y nombre determinado
def guardar_imagen(imagen, directorio_destino = './multimedia/img/'):
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

# Función para suspender x minutos
def suspender_programa(minutos):
    # Convertir minutos a segundos
    segundos = minutos * 60
    # Suspender el programa durante el tiempo especificado
    time.sleep(segundos)

# Función principal para que se descargue una imagen cada minuto
def main():
    print("Starting imgDownloader.py")

    # URL de la página web
    url_pagina = configs.url_webcam


    try:
        while True:
            img = dw.descargar_imagen(url_pagina)
            guardar_imagen(img)
            suspender_programa(1.05)
    except KeyboardInterrupt:
        print("\nCtrl + C detectado. Deteniendo el programa imgDownloader.py.")

if __name__ == "__main__":
    main()

import requests
import cv2
import numpy as np
import yolo_object_detector.yolo_detector_function as yolo

# Programa para monitorizar las personas que pasan por la camara web

# Función para descargar imagen de url
def descargar_imagen(url):
    try:
        # Definir un User-Agent personalizado
        headers = {'User-Agent': 'Mozilla/5.0'}

        # Realizar la solicitud GET a la URL con el User-Agent personalizado
        respuesta = requests.get(url, headers=headers)
        
        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            print("Imagen descargada exitosamente")
            # Convertir la imagen descargada a un arreglo numpy
            nparr = np.frombuffer(respuesta.content, np.uint8)
            # Decodificar el arreglo numpy en una imagen OpenCV
            return cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        else:
            print("Error al descargar la imagen. Código de estado:", respuesta.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

# Función para mostrar imagen
def mostrar_imagen(img_cv):
    try:
        # Mostrar la imagen en una ventana
        cv2.imshow('Imagen Descargada', img_cv)
        # Esperar 5 segundos antes de descargar la siguiente imagen
        cv2.waitKey(15000)  # Esperar 15 segundos (15000 ms)
        # Cerrar la ventana de la imagen
        cv2.destroyWindow('Imagen Descargada')
    except Exception as e:
        print("Ocurrió un error al mostrar la imagen:", str(e))


def main():
    print("Iniciando imgDownloader.py")

    # URL de la página web
    url_pagina = 'https://www.acifalcoi.com/webcam/menejador.jpg'

    while True:
        img = descargar_imagen(url_pagina)
        yolo_img = yolo.detect_objects(img)
        # Mostrar la imagen
        mostrar_imagen(yolo_img[0])

if __name__ == "__main__":
    main()

import cv2
import numpy as np
import os

def mascara(image):
    # Cargar la máscara
    mask = cv2.imread("./mascara/mascara1.jpg", cv2.IMREAD_GRAYSCALE)


    # Aplicar la máscara a la imagen
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image

def detector_movimiento(img_anterior, img_actual):
    # Pasamos las imagenes a escala de grises
    img_anterior_gris = cv2.cvtColor(img_anterior, cv2.COLOR_BGR2GRAY)
    img_actual_gris = cv2.cvtColor(img_actual, cv2.COLOR_BGR2GRAY)


    # Comparamos la imagen actual con la anterior para ver si ha habido algun cambio
    dif = cv2.absdiff(img_anterior_gris, img_actual_gris)
    _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)

    # Insertamos una mascara para tapar las partes de la imagen que no nos interesan
    th = mascara(th)

    # Detectamos los contornos de la diferencia de la imagen
    cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Contador para contar el número de personas
    n_personas = 0

    # Iteramos por todos los contornos y nos quedamos con los objetos más grandes
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 500 and area < 3000:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img_actual, (x,y), (x+w,y+h),(0,255,0),2)
            n_personas+=1
    
    if n_personas == 0:
        return None
    
    return img_actual

ruta_carpeta = "./img/"
ruta_carpeta = "/Volumes/MULTIMEDIA2/downloads/img/"


# Obtener la lista de imágenes en el directorio "img"
imagenes = os.listdir(ruta_carpeta)
imagenes.sort()

anterior = None


print(imagenes)

anterior =  actual = cv2.imread(ruta_carpeta + imagenes[0])

# Iterar sobre cada imagen en la lista
for imagen in imagenes:
    # Construir la ruta completa de la imagen
    ruta_imagen = ruta_carpeta + imagen
    
    # Leer la imagen y convertirla a escala de grises
    actual = cv2.imread(ruta_imagen)

    if anterior is not None:
        det_movimiento = detector_movimiento(anterior, actual)
        if det_movimiento is not None:
            cv2.imshow("Imagen", det_movimiento)
            cv2.waitKey(0)
    else:
        anterior = actual



# Cerrar todas las ventanas después de mostrar todas las imágenes
cv2.destroyAllWindows()

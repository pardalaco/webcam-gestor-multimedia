import cv2
import numpy as np
import os

def mascara(image):
    # Cargar la máscara
    mask = cv2.imread("./mascara/mascara.jpg", cv2.IMREAD_GRAYSCALE)


    # Aplicar la máscara a la imagen
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image

def detector_movimiento(img_anterior, img_actual):
    # Comparamos la imagen actual con la anterior para ver si ha habido algun cambio
    dif = cv2.absdiff(img_anterior, img_actual)
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
        if area > 700:
            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(img_actual, (x,y), (x+w,y+h),(0,255,0),2)
            n_personas+=1
    
    if n_personas == 0:
        return None
    
    return img_actual


# Obtener la lista de imágenes en el directorio "img"
imagenes = os.listdir("./img")
imagenes.sort()

anterior = None


print(imagenes)

# Iterar sobre cada imagen en la lista
for imagen in imagenes:
    # Construir la ruta completa de la imagen
    ruta_imagen = "./img/" + imagen
    
    # Leer la imagen y convertirla a escala de grises
    img = cv2.imread(ruta_imagen)
    actual = img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if anterior is not None:
        dif = cv2.absdiff(anterior, actual)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)

        th = mascara(th)

        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(img, cnts, -1, (0,0,255),2)

        for c in cnts:
            area = cv2.contourArea(c)
            if area > 700:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),2)


    anterior = actual

    # Mostrar la imagen
    cv2.imshow("Imagen", img)
    cv2.waitKey(0)

# Cerrar todas las ventanas después de mostrar todas las imágenes
cv2.destroyAllWindows()

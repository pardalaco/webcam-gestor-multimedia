import cv2
import os

def mascara(image):
    # Cargar la máscara
    mask = cv2.imread("./mascara/mascara1.jpg", cv2.IMREAD_GRAYSCALE)


    # Aplicar la máscara a la imagen
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image

def detect_upper_bodies(image):
    # Cargar el clasificador preentrenado
    upperbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Le aplicamos una mascara para indicarle al algoritmo que partes de la imagen nos interesan
    img_gray_mask = mascara(gray)



    # Detectar cuerpos superiores en la imagen
    upperbodies = upperbody_cascade.detectMultiScale(img_gray_mask, 1.04, 3)

    # Dibujar rectángulos alrededor de los cuerpos superiores detectados
    for (x, y, w, h) in upperbodies:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(upperbodies) == 0:
        return None
    return image

ruta_carpeta = "./img/personas/"
ruta_carpeta = "/Volumes/MULTIMEDIA2/downloads/img1/"


imagenes = os.listdir(ruta_carpeta)

print(imagenes)

imagenes.sort()

for imagen in imagenes:
    ruta_imagen = ruta_carpeta + imagen
    img = cv2.imread(ruta_imagen)

    img = detect_upper_bodies(img)

    if img is not None:
        cv2.imshow(imagen, img)
        cv2.waitKey(0)

cv2.destroyAllWindows()

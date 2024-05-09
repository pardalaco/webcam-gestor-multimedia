import cv2
import numpy as np

def apply_mask(image_path, mask_path):
    # Cargar la imagen y la máscara
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)


    # Aplicar la máscara a la imagen
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # Mostrar la imagen resultante
    cv2.imshow("Masked Image", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ruta de la imagen y la máscara
image_path = "imagen.jpg"  # Reemplaza "imagen.jpg" con la ruta de tu imagen
mask_path = "mascara.jpg"  # Reemplaza "mascara.jpg" con la ruta de tu máscara

# Aplicar la máscara a la imagen
apply_mask(image_path, mask_path)

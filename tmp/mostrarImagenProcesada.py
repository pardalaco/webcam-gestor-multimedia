import yolo_object_detector.yolo_detector_function as yolo
import cv2

# Cargar la imagen
imagen = cv2.imread('img/menejador_alcoi_2024-05-19_08_40_06.jpg')
imagen = yolo.detect_objects(imagen)

# Verificar si la imagen fue cargada correctamente
if imagen is None:
    print("Error al cargar la imagen")
else:
    # Mostrar la imagen en una ventana
    print(imagen[1])
    cv2.imshow('Mi Imagen', imagen[0])

    # Esperar a que se presione una tecla para cerrar la ventana
    cv2.waitKey(0)

    # Cerrar todas las ventanas abiertas por OpenCV
    cv2.destroyAllWindows()

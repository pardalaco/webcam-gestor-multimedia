import cv2
import os

def crear_video_desde_imagenes(ruta_carpeta, nombre_video_salida='output_video.mp4', fps=30):
    # Obtener la lista de nombres de archivos en la carpeta
    lista_archivos = os.listdir(ruta_carpeta)
    # Filtrar solo los archivos de imagen (puedes ajustar esta lógica según tus necesidades)
    lista_imagenes = [archivo for archivo in lista_archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not lista_imagenes:
        print("No se encontraron imágenes en la carpeta.")
        return
    
    # Ordenar las imágenes por nombre de archivo
    lista_imagenes.sort()
    

    # Obtener el primer archivo de imagen para obtener el tamaño
    primer_imagen = cv2.imread(os.path.join(ruta_carpeta, lista_imagenes[0]))
    altura, ancho, _ = primer_imagen.shape
    
    # Configurar el codec de video y el objeto VideoWriter
    codec = cv2.VideoWriter_fourcc(*'XVID')
    video_salida = cv2.VideoWriter(nombre_video_salida, codec, fps, (ancho, altura))
    
    # Iterar sobre cada imagen, agregarla al video y escribir el video
    for imagen_nombre in lista_imagenes:
        ruta_imagen = os.path.join(ruta_carpeta, imagen_nombre)
        imagen = cv2.imread(ruta_imagen)
        video_salida.write(imagen)
        print(imagen_nombre)
    
    # Liberar el objeto VideoWriter y mostrar un mensaje de finalización
    video_salida.release()
    print(f"¡Video '{nombre_video_salida}' creado exitosamente!")

# Ejemplo de uso
ruta_carpeta = '/Volumes/USB_C_DANI/08_programacio/Menejador/img/'
nombre_video_salida = 'video_salida.mp4'
crear_video_desde_imagenes(ruta_carpeta, nombre_video_salida)

import cv2
import os
import yolo_object_detector.yolo_detector_function as yolo

# Función a la que se le pasa una ruta de una carpeta analiza las imagenes y genera un video
def crear_video_desde_imagenes(ruta_carpeta_entrada_video, nombre_video_salida='output_video', ruta_video_salida='./multimedia/video/sin_procesar/', formato='.mp4', fps=30):
    # Verificar si la ruta de salida existe, si no, crearla
    if not os.path.exists(ruta_video_salida):
        os.makedirs(ruta_video_salida)
        print("Carpeta creada: "+ruta_video_salida)

    # Obtener la lista de nombres de archivos en la carpeta
    lista_archivos = os.listdir(ruta_carpeta_entrada_video)
    # Filtrar solo los archivos de imagen (puedes ajustar esta lógica según tus necesidades)
    lista_imagenes = [archivo for archivo in lista_archivos if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not lista_imagenes:
        print("No se encontraron imágenes en la carpeta.")
        return
    
    # Ordenar las imágenes por nombre de archivo
    lista_imagenes.sort()
    
    # Obtener el primer archivo de imagen para obtener el tamaño
    primer_imagen = cv2.imread(os.path.join(ruta_carpeta_entrada_video, lista_imagenes[0]))
    altura, ancho, _ = primer_imagen.shape
    
    # Configurar el codec de video y el objeto VideoWriter
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    video_salida = cv2.VideoWriter(os.path.join(ruta_video_salida, nombre_video_salida + formato), codec, fps, (ancho, altura))
    
    # Iterar sobre cada imagen, agregarla al video y escribir el video
    for imagen_nombre in lista_imagenes:
        ruta_imagen = os.path.join(ruta_carpeta_entrada_video, imagen_nombre)
        imagen = cv2.imread(ruta_imagen)
        video_salida.write(imagen)
        print("Video > "+imagen_nombre)
    
    # Liberar el objeto VideoWriter y mostrar un mensaje de finalización
    video_salida.release()
    print(f"¡Video '{nombre_video_salida}{formato}' creado exitosamente en '{ruta_video_salida}'!")

# Función la cual se le pasa la ruta de un video y usando la librería yolo detecta objetos/personas...
def procesar_video(ruta_video, nombre_video_salida='output_video', ruta_video_salida='./multimedia/video/procesado/', formato='.mp4', fps=30):
    # Verificar si la ruta de salida existe, si no, crearla
    if not os.path.exists(ruta_video_salida):
        os.makedirs(ruta_video_salida)
        print("Carpeta creada: "+ruta_video_salida)

    # Leer el video de entrada
    cap = cv2.VideoCapture(ruta_video)
    if not cap.isOpened():
        print("Error: No se puede abrir el video "+ruta_video+".")
        return

    # Obtener ancho y alto de los frames del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Definir el codec y crear el objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec para .mp4
    out = cv2.VideoWriter(os.path.join(ruta_video_salida, nombre_video_salida + formato), fourcc, fps, (width, height))

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_procesados = 0

    while True:
        ret, frame = cap.read()  # Leer frame por frame
        if not ret:
            break

        # Procesar el frame usando la función detect_objects
        frame_procesado = yolo.detect_objects(frame)

        # Escribir el frame procesado en el video de salida
        out.write(frame_procesado[0])

        # Incrementar el contador de frames procesados
        frames_procesados += 1

        # Calcular el porcentaje de avance
        porcentaje_avance = (frames_procesados / total_frames) * 100

        # Imprimir el porcentaje de avance
        print(f"{nombre_video_salida} Procesando... {porcentaje_avance:.2f}% completado", end='\r')

    # Liberar los objetos VideoCapture y VideoWriter
    cap.release()
    out.release()

    print(f"\n¡Video '{nombre_video_salida}{formato}' creado y procesado exitosamente en '{ruta_video_salida}'!")

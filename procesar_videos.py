import os
import video

def procesar_videos_en_carpeta(carpeta_entrada):
    # Obtener la lista de archivos en la carpeta de entrada
    archivos_en_carpeta = os.listdir(carpeta_entrada)
    
    print(archivos_en_carpeta)

    # Iterar sobre los archivos
    for archivo in archivos_en_carpeta:
        # Verificar si el archivo es un video
        if archivo.endswith(('.mp4', '.avi', '.mov')):  # Puedes agregar más extensiones si es necesario
            # Construir las rutas de entrada y salida
            ruta_video = os.path.join(carpeta_entrada, archivo)
            nombre_video_salida = os.path.splitext(archivo)[0]  # Usar el mismo nombre de archivo sin la extensión
            
            # Procesar el video
            video.procesar_video(ruta_video, nombre_video_salida)
            print(f"Video procesado: {archivo}")

# Ejemplo de uso
carpeta_entrada = './video/sin_procesar/'
procesar_videos_en_carpeta(carpeta_entrada)

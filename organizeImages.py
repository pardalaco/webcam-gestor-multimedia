import os
import shutil

# Función para obtener la fecha de un nombre de archivo
def obtener_fecha(nombre_archivo):
    partes = nombre_archivo.split("_")
    if len(partes) >= 4:
        fecha = partes[2]
        return fecha
    else:
        return None

# Directorio donde se encuentran las imágenes
directorio_imagenes = "/Volumes/USB_C_DANI/08_programacio/Menejador/img/"

# Obtener lista de archivos en el directorio
archivos = os.listdir(directorio_imagenes)

# Crear carpeta para cada día y mover las imágenes correspondientes
for archivo in archivos:
    fecha = obtener_fecha(archivo)
    print(archivo)
    if fecha:
        # Crear la carpeta si no existe
        carpeta_destino = os.path.join(directorio_imagenes, fecha)
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        # Mover el archivo a la carpeta correspondiente
        shutil.move(os.path.join(directorio_imagenes, archivo), os.path.join(carpeta_destino, archivo))

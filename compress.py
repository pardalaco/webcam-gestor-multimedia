import os
import datetime
import shutil
import zipfile

# Función para comprimir y eliminar las carpetas de hace más de 5 días
def comprimir_carpetas_antiguas(ruta_carpeta="./multimedia/img/", dias=5, ruta_guardado="./multimedia/zips/"):
    # Verificar si la carpeta de entrada existe
    if not os.path.isdir(ruta_carpeta):
        print(f"La carpeta a comprimir {ruta_carpeta} no existe.")
        return
    
    # Verificar si la carpeta de guardado existe, si no, intentar crearla
    if not os.path.isdir(ruta_guardado):
        print(f"La carpeta de guardado {ruta_guardado} no existe.")
        return

    
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()

    # Recorrer los archivos y carpetas en la ruta especificada
    for nombre_carpeta in os.listdir(ruta_carpeta):
        ruta_carpeta_completa = os.path.join(ruta_carpeta, nombre_carpeta)
        
        # Verificar si es una carpeta
        if os.path.isdir(ruta_carpeta_completa):
            # Extraer la fecha del nombre de la carpeta
            try:
                fecha_carpeta = datetime.datetime.strptime(nombre_carpeta, "%Y-%m-%d")
            except ValueError:
                continue  # Ignorar carpetas que no tienen el formato de fecha correcto
                
            # Calcular la diferencia de días
            diferencia_dias = (fecha_actual - fecha_carpeta).days
            
            # Comprimir la carpeta si tiene más de 'dias' días
            if diferencia_dias > dias:
                nombre_zip = f"{nombre_carpeta}.zip"
                ruta_zip = os.path.join(ruta_guardado, nombre_zip)
                with zipfile.ZipFile(ruta_zip, 'w') as zip_ref:
                    # Recorrer los archivos en la carpeta y agregarlos al zip
                    for carpeta_raiz, _, archivos in os.walk(ruta_carpeta_completa):
                        for archivo in archivos:
                            ruta_completa = os.path.join(carpeta_raiz, archivo)
                            ruta_relativa = os.path.relpath(ruta_completa, ruta_carpeta_completa)
                            zip_ref.write(ruta_completa, ruta_relativa)
                
                # Eliminar la carpeta después de comprimir
                shutil.rmtree(ruta_carpeta_completa)
                
                print(f"Carpeta {nombre_carpeta} comprimida y eliminada correctamente.")


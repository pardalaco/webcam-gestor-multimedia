import compress, video
import time
from datetime import datetime, timedelta

def wait_midnight():
    # Calcular cuánto tiempo falta hasta la medianoche
    ahora = time.localtime()
    segundos_hasta_medianoche = 86400 - (ahora.tm_hour * 3600 + ahora.tm_min * 60 + ahora.tm_sec)
    
    segundos_hasta_medianoche += 5 * 60

    # Suspender el programa hasta la medianoche
    time.sleep(segundos_hasta_medianoche)

def get_date_previous_day():
    fecha_actual = datetime.now() - timedelta(days=1)
    fecha_anterior = fecha_actual.strftime('%Y-%m-%d')
    return fecha_anterior



while True:
    wait_midnight()
    print("Daily routine running...")

    # Comprimir carpetas
    compress.comprimir_carpetas_antiguas()

    # Generate video
    nombre_video_salida = get_date_previous_day()
    ruta_carpeta_entrada_video="./img/" + nombre_video_salida
    video.crear_video_desde_imagenes(ruta_carpeta_entrada_video, nombre_video_salida)


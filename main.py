import multiprocessing
import imgDownloader
import dailyRoutine
import signal

def stop_programs(signum, frame):
    print("\nCtrl + C detectado. Deteniendo los programas...")
    process1.terminate()
    process2.terminate()
    print("Programas detenidos correctamente.")

if __name__ == "__main__":
    print("Runing main.py")

    signal.signal(signal.SIGINT, stop_programs)  # Capturar la señal Ctrl + C

    # Crear procesos para ejecutar los programas
    process1 = multiprocessing.Process(target=imgDownloader.main)
    process2 = multiprocessing.Process(target=dailyRoutine.main)

    # Iniciar los procesos
    process1.start()
    process2.start()

    # Esperar a que ambos procesos terminen
    process1.join()
    process2.join()

    print("Ambos programas han terminado de ejecutarse.")

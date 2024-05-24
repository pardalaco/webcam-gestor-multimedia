

# webcamGestorMultimedia

`webcamGestorMultimedia` es un programa diseñado para conectarse a una cámara web, descargar imágenes a intervalos regulares y almacenar estas imágenes en el directorio `./multimedia/img/nombre_del_dia`. A las 00:05 de la noche, el programa crea un video con las imágenes del día y lo procesa utilizando la librería YOLO (You Only Look Once) para detectar personas, generando un video con las detecciones.

## Requisitos

Asegúrate de tener instalado Python y las siguientes dependencias. Puedes instalarlas fácilmente utilizando el archivo `requirements.txt` proporcionado:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye:

```
opencv-python
requests
numpy
```

Por favor, asegúrese de descargar el archivo [yolov3.weights](https://pjreddie.com/media/files/yolov3.weights) o puede encontrarlo en la página [opencv-tutorial.readthedocs.io](https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html). Coloque este archivo dentro de la carpeta `yolo_object_detector/model` para que el programa funcione correctamente.


## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/webcamGestorMultimedia.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd webcamGestorMultimedia
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Descarga el archivo yolov3.weights desde aquí o desde la página y colócalo dentro de la carpeta `yolo_object_detector/model`.
5. Instala las dependencias:
   ```bash
   python3 main.py
   ```

## Uso

Para ejecutar el programa, simplemente corre el siguiente comando en tu terminal:

```bash
python main.py
```

El programa se encargará de:

1. Conectarse a la cámara web y capturar imágenes a intervalos regulares.
2. Guardar las imágenes en el directorio `./multimedia/img/nombre_del_dia`.
3. A las 00:05 de la noche, crear un video con las imágenes capturadas del día.
4. Procesar el video utilizando la librería YOLO para detectar personas y generar un video con las detecciones.

## Estructura del Proyecto

Claro, aquí tienes la parte de la estructura del proyecto actualizada con la información sobre la carpeta `zips`:

Aquí está la estructura del proyecto actualizada para incluir la información sobre las carpetas `video` con las subcarpetas `sin_procesar` y `procesado`:


```
webcamGestorMultimedia/
│
├── multimedia/
│   ├── img/
│   │   └── nombre_del_dia/
│   │       ├── img1.jpg
│   │       ├── img2.jpg
│   │       └── ...
│   ├── zips/
│   │   ├── nombre_del_dia.zip
│   │   ├── nombre_del_otro_dia.zip
│   │   └── ...
│   └── video/
│       ├── yolo_detector_function.py
│       ├── sin_procesar/
│       │   ├── nombre_del_dia.mp4
│       │   ├── nombre_del_otro_dia.mp4
│       │   └── ...
│       └── procesado/
│           ├── nombre_del_dia.mp4
│           ├── nombre_del_otro_dia.mp4
│           └── ...
│
├── yolo_object_detector/
│   └── model/
│       ├── coco.names
│       ├── yolov3.cfg
│       └── yolov3.weights
│
├── compress.py
├── configs.py
├── dailyRoutine.py
├── imgDownloader.py
├── imgSaver.py
│
├── main.py
├── requirements.txt
└── README.md
```




Este fragmento describe cómo se organiza el directorio `multimedia` con las subcarpetas `img` para las imágenes diarias y `zips` para las compresiones de las carpetas de los días que contienen las imágenes.

## Notas

- Asegúrate de que la cámara web está correctamente conectada y configurada.
- No te olvides de configurar el programa accediendo al fichero `configs.py`.



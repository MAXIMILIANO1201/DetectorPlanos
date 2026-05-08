# DetectorPlanos

Librería en Python para la detección de líneas, esquinas e intersecciones en planos arquitectónicos usando OpenCV.

## Características

- Detección de bordes con Canny
- Detección de líneas con Hough Transform
- Detección de esquinas con Harris
- Detección de intersecciones geométricas
- Visualización de resultados

## Estructura del proyecto

```plaintext
DetectorPlanos/
│
├── DetectorPlanos/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── detection.py
│   ├── geometry.py
│
├── Ejemplos/
│   ├── demo.py
│   └── plano.png
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:35:47 2026

@author: adria
"""
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

import cv2
import matplotlib.pyplot as plt

from DetectorPlanos.preprocessing import *
from DetectorPlanos.detection import *
from DetectorPlanos.geometry import *

# ============================================================
# CARGAR IMAGEN
# ============================================================

# ============================================================
# CARGAR IMAGEN
# ============================================================

nombre = input("Ingresa el nombre de la imagen: ")

ruta = os.path.join(os.path.dirname(__file__), nombre)

img = cv2.imread(ruta)

if img is None:
    print("Error: no se pudo cargar la imagen")
    sys.exit()
# ============================================================
# PREPROCESAMIENTO
# ============================================================

gris = convertir_grises(img)

binaria = binarizar_otsu(gris)

bordes = detectar_bordes(gris)

# ============================================================
# DETECCIÓN
# ============================================================

lineas = detectar_lineas(bordes)

esquinas, mapa_harris = detectar_esquinas_harris(gris)

intersecciones = detectar_intersecciones(lineas)

# ============================================================
# VISUALIZACIÓN
# ============================================================

resultado = img.copy()

# Dibujar líneas
for (x1, y1, x2, y2) in lineas:

    cv2.line(
        resultado,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        2
    )

# Dibujar esquinas
for (x, y) in esquinas:

    cv2.circle(
        resultado,
        (x, y),
        2,
        (0, 0, 255),
        -1
    )

# Dibujar intersecciones
for (x, y) in intersecciones:

    cv2.circle(
        resultado,
        (x, y),
        5,
        (255, 0, 0),
        -1
    )

# ============================================================
# RESULTADOS
# ============================================================

print("Número de líneas:", len(lineas))
print("Número de esquinas:", len(esquinas))
print("Número de intersecciones:", len(intersecciones))

plt.figure(figsize=(12, 8))

plt.subplot(2,2,1)
plt.imshow(gris, cmap='gray')
plt.title("Escala de grises")

plt.subplot(2,2,2)
plt.imshow(bordes, cmap='gray')
plt.title("Bordes Canny")

plt.subplot(2,2,3)
plt.imshow(binaria, cmap='gray')
plt.title("Binarización")

plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB))
plt.title("Resultado final")

plt.tight_layout()
plt.show()
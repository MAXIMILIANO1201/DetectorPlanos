# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:28:40 2026

@author: adria
"""

import cv2
import numpy as np


def detectar_lineas(bordes):

    lineas = cv2.HoughLinesP(
        bordes,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=40,
        maxLineGap=10
    )

    segmentos = []

    if lineas is not None:

        for l in lineas:

            x1, y1, x2, y2 = l[0]

            segmentos.append((x1, y1, x2, y2))

    return segmentos


def detectar_esquinas_harris(img_gris):

    gris_float = np.float32(img_gris)

    harris = cv2.cornerHarris(
        gris_float,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    harris = cv2.dilate(harris, None)

    puntos = np.argwhere(
        harris > 0.01 * harris.max()
    )

    esquinas = []

    for y, x in puntos:

        esquinas.append((x, y))

    return esquinas, harris
import numpy as np


def detectar_lineas(bordes):

    lineas = cv2.HoughLinesP(
        bordes,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=40,
        maxLineGap=10
    )

    segmentos = []

    if lineas is not None:

        for l in lineas:

            x1, y1, x2, y2 = l[0]

            segmentos.append((x1, y1, x2, y2))

    return segmentos


def detectar_esquinas_harris(img_gris):

    gris_float = np.float32(img_gris)

    harris = cv2.cornerHarris(
        gris_float,
        blockSize=2,
        ksize=3,
        k=0.04
    )

    harris = cv2.dilate(harris, None)

    puntos = np.argwhere(
        harris > 0.01 * harris.max()
    )

    esquinas = []

    for y, x in puntos:

        esquinas.append((x, y))

    return esquinas, harris
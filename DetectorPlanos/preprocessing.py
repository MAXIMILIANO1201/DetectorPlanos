# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:27:30 2026

@author: adria
"""
import cv2

def convertir_grises(img):

    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def aplicar_blur(img_gris):

    return cv2.GaussianBlur(img_gris, (5, 5), 1.2)


def binarizar_otsu(img_gris):

    _, binaria = cv2.threshold(
        img_gris,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    return binaria


def detectar_bordes(img_gris):

    blur = aplicar_blur(img_gris)

    bordes = cv2.Canny(blur, 50, 150)

    return bordes
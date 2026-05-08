# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:29:17 2026

@author: adria
"""

def interseccion_segmentos(seg1, seg2):

    x1, y1, x2, y2 = seg1
    x3, y3, x4, y4 = seg2

    den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)

    if den == 0:
        return None

    px = (
        ((x1*y2 - y1*x2)*(x3 - x4) -
        (x1 - x2)*(x3*y4 - y3*x4))
        / den
    )

    py = (
        ((x1*y2 - y1*x2)*(y3 - y4) -
        (y1 - y2)*(x3*y4 - y3*x4))
        / den
    )

    if (
        min(x1, x2) <= px <= max(x1, x2)
        and
        min(y1, y2) <= py <= max(y1, y2)
        and
        min(x3, x4) <= px <= max(x3, x4)
        and
        min(y3, y4) <= py <= max(y3, y4)
    ):

        return (int(px), int(py))

    return None


def detectar_intersecciones(lineas):

    intersecciones = []

    n = len(lineas)

    for i in range(n):

        for j in range(i + 1, n):

            p = interseccion_segmentos(
                lineas[i],
                lineas[j]
            )

            if p is not None:

                intersecciones.append(p)

    return list(set(intersecciones))
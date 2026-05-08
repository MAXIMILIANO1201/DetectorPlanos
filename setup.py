# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:06:52 2026

@author: adria
"""

from setuptools import setup, find_packages

setup(
    name="DetectorPlanos",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "numpy",
        "matplotlib",
        "scipy"
    ],
    author="Adriana, Maximiliano, Adrian, Luis Angel",
    description="Librería para detección de líneas, esquinas e intersecciones en planos arquitectónicos"
)
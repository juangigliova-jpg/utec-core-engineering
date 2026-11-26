#!/usr/bin/env python3
"""Módulo que define la clase Rectangle, hija de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectángulo definido por su ancho y su altura."""

    def __init__(self, width, height):
        """Inicializa el rectángulo validando ancho y alto.

        Args:
            width (int): Ancho, entero positivo.
            height (int): Alto, entero positivo.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

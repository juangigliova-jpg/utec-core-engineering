#!/usr/bin/env python3
"""Módulo que define la clase Square, hija de Rectangle, con representación en cadena."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Cuadrado: rectángulo con ancho y alto iguales."""

    def __init__(self, size):
        """Inicializa el cuadrado validando su tamaño.

        Args:
            size (int): Tamaño del lado, entero positivo.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calcula el área del cuadrado."""
        return super().area()

    def __str__(self):
        """Devuelve la descripción del cuadrado."""
        return "[Square] {}/{}".format(self.__size, self.__size)

#!/usr/bin/env python3
"""Módulo que define la clase base BaseGeometry para figuras geométricas."""


class BaseGeometry:
    """Clase base con comportamiento compartido para figuras geométricas."""

    def area(self):
        """Calcula el área de la figura.

        Raises:
            Exception: Siempre, porque cada subclase debe implementarlo.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo.

        Args:
            name (str): Nombre del parámetro, usado en los mensajes de error.
            value: Valor a validar.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor o igual que 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
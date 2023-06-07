# -*- coding: utf-8 -*-

"""ACTIVIDAD 01 - SEMANA 02

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 06-06-2023

Ejercicio 1. Escriba un programa que convierta un valor dado en grados
Fahrenheit a grados Celsius.

Ejercicio 2. Dados dos números, mostrar la suma, resta, división y
multiplicación.

Ejercicio 3. Calcular el perímetro y área de un rectángulo dada su base
y altura.

Ejercicio 4. Calcular la media de tres números ingresados por teclado."""


class Rectangulo:
    """Se usa para el ejericio 3."""

    def __init__(self, base=0, altura=0) -> None:
        self._base = base
        self._altura = altura

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, new_base: float):
        self._base = new_base if new_base > 0 else 0

    @property
    def altura(self) -> float:
        return self._altura

    @altura.setter
    def altura(self, new_altura: float):
        self._altura = new_altura if new_altura > 0 else 0

    def get_area(self):
        return self._base * self._altura

    def get_perimeter(self):
        return 2 * (self._base + self._altura)

    def __str__(self) -> str:
        return 'Rectangulo{base=%.2f, altura=%.2f}' % (self._base, self._base)


def fahrenhit_to_celcius(f_degrees: float) -> float:
    """Ejercicio 1."""
    if f_degrees < -459.67:
        raise Exception('No hay nada tan frio en el universo')
    return (f_degrees-32) * 5/9


def mostrar_operaciones(x: float, y: float):
    """Ejericio 2."""
    print('OPERANDOS     : x =', x, ", y =", y)
    print('suma          :', x+y)
    print('resta         :', x-y)
    print('multiplicacion:', x*y)
    print('division      :', x/y) if y != 0 else print('Divisor y no puede ser cero')


def media_aritmetica(*numbers) -> float:
    """Ejericio 4"""
    total = 0
    for n in numbers:
        total += n
    return total/len(numbers)


# EJECUCIÓN
if __name__ == '__main__':

    print("EJERCICIO 1: 123F a Celsius")
    print(fahrenhit_to_celcius(123), end='\n\n')

    print('EJERCICIO 2: operando 2 y 5')
    mostrar_operaciones(2, 5)
    print()

    rectangulo = Rectangulo(2, 10)
    print("EJERCICIO 3:", rectangulo)
    print('area      =', rectangulo.get_area(), 'u^2')
    print('perimetro =', rectangulo.get_perimeter(), 'u')
    print()

    print('MEDIA ARITMÉTICA DE 3 NÚMEROS:')
    entradas = [float(input('>>> ')) for _ in range(3)]
    print('Resultado =', media_aritmetica(*entradas))

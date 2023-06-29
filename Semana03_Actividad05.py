"""ACTIVIDAD 05 - SEMANA 03

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 13-06-2023

Ejercicio 1. Programa que imprima si un número es positivo o negativo.
Ejercicio 2. Programa que imprima si número está en el rango de 1 a 7.
Ejercicio 3. Programa que calcule el interés de una cantidad si es
mayor al 30%, si no informa el importe total.
"""


def positivo_o_negativo(n: int):
    if n < 0:
        print('Negativo')
    elif n == 0:
        print('neutro')
    else:
        print('Positivo')


def en_rango(n: int):
    if n >= 1 and n <= 7:
        print('En rango')
    else:
        print('Fuera de rango')


def calcular_interes(cantidad, porcentaje):
    if porcentaje < 0 or porcentaje > 100 or cantidad < 0:
        raise ValueError('Verifique sus argumentos')
    if porcentaje > 30:
        return cantidad
    return cantidad*(1 + 1/porcentaje)


# Ejercicio 1.
print('Ejercicio 01')
positivo_o_negativo(-1)
positivo_o_negativo(0)
positivo_o_negativo(1)
print('-'*50)

# Ejercicio 2.
print('Ejercicio 02')
en_rango(-1)
en_rango(1)
en_rango(7)
en_rango(8)
print('-'*50)

# Ejercicio 3.
print(calcular_interes(1000, 10))
print(calcular_interes(1000, 30))
print(calcular_interes(1000, 50))

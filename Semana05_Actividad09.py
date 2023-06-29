# -*- coding: utf-8 -*-

"""ACTIVIDAD 09 - SEMANA 05

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 23-06-2023

Ejercicio 1. Realice un programa que pregunte aleatoriamente una 
multiplicación. El programa debe indicar si la respuesta ha sido correcta 
o no (en caso que la respuesta sea incorrecta el programa debe indicar 
cuál es la correcta). 
El programa preguntará 10 multiplicaciones, 
y al finalizar mostrará el número de aciertos.

Ejercicio 2. Obtener el cuadrado de todos los elementos en la lista.
Lista: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

Ejercicio 3. Obtener la cantidad de elementos mayores a 5 en la tupla.
tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)

Ejercicio 4. Obtener la suma de todos los elementos en la lista.
"""
import random


# ejercicio 1
print('Ejercicio 1', '-'*20)
respuestas = {'correctas': 0, 'incorrectas': 0}
for _ in range(10):
    n1 = random.randint(1, 10)
    n2 = random.randint(1, 10)
    print('Cuanto es %2d X %2d ? ' % (n1, n2))
    respuesta = int(input('>>> '))
    if respuesta == n1*n2:
        print('Respuesta correcta!')
        respuestas['correctas'] += 1
    else:
        print('Respuesta incorrecta')
        print('La respuesta correcta es: ', n1*n2)
        respuestas['incorrectas'] += 1

print('Resultados: ', respuestas, end='\n\n')

# ejercicio 2
print('Ejercicio 2', '-'*20)
lista = [i for i in range(1, 11)]
cuadrados = list(map(lambda x: x**2, lista))
print('Cuadrados:', cuadrados, end='\n\n')


# ejercicio 3
print('Ejercicio 3', '-'*20)
tupla = (5, 2, 6, 7, 8, 10, 77, 55, 2, 1, 30, 4, 2, 3)
mayores_a_5 = list(filter(lambda x: x > 5, tupla))
print('Mayores a 5:', mayores_a_5, '\n\n')

# ejercicio 4
print('Ejercicio 3', '-'*20)
suma = sum(lista)
print('La suma de los elementos en', lista)
print('es:', suma, end='\n\n')

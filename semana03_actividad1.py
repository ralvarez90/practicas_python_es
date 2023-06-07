# -*- coding: utf-8 -*-
from random import randint

"""ACTIVIDAD 01 - SEMANA 03

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 06-06-2023

Ejercicio 1. Realizar un programa que inicialice una lista con 10 
valores aleatorios (del 1 al 10) y posteriormente muestre en 
pantalla cada elemento de la lista junto con su cuadrado 
y su cubo.

Ejercicio 2. Crea una lista e inicializarla con 5 cadenas de 
caracteres leídas por teclado. Copia los elementos de la lista 
en otra lista pero en orden inverso, 
y muestra sus elementos por la pantalla.

Ejercicio 3. Se quiere realizar un programa que lea por teclado 
las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10). 
A continuación debe mostrar todas las notas, la nota media, 
la nota más alta que ha sacado y la menor.

Ejercicio 4. 
"""


# EJECUCIÓN
if __name__ == '__main__':

    # Ejercicio 1
    print('EJERCICIO 1: Muestra numero, su cuadrado y su cubo')
    aleatorios = [randint(1, 10) for _ in range(10)]
    for n in aleatorios:
        print('%3d,  %3d,  %3d' % (n, n**2, n**3))
    print('-'*50)

    # Ejercicio 2
    print('EJERCICIO 2: Ingrese de palabras')
    words = [input('>>> ') for _ in range(5)]
    reverse_words_copy = words[::-1]
    print('Original   :', words)
    print('En reversa :', reverse_words_copy)
    print('-'*50)

    # Ejercicio 3
    print('EJERCICIO 3: Leer 10 notas entre 0 y 10')
    total_calificaciones = 0
    notas = []
    while total_calificaciones < 10:
        calif = int(input(f'calificacion {total_calificaciones+1:2d} : '))
        if calif >= 0 and calif <= 10:
            notas.append(calif)
            total_calificaciones += 1
    print('Notas ingresadas : ', notas)
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas)/len(notas)
    print('Nota mayor:', mayor)
    print('Nota menor:', menor)
    print('Media     :', media)
    print('-'*50)

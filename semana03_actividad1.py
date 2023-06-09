# -*- coding: utf-8 -*-
from random import randint

"""ACTIVIDAD 04 - SEMANA 03

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

Ejercicio 4. Codifica un programa que nos permita guardar los nombres
de los alumnos de una clase y las notas que han obtenido. Cada alumno
puede tener distinta cantidad de notas. Guarda la información en un 
diccionario cuya claves serán los nombres de los alumnos y los valores 
serán listados con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá 
su nombre e irá pidiendo sus notas hasta que introduzcamos un número 
negativo. Al final el programa nos mostrará la lista de alumnos y la 
nota media obtenida por cada uno de ellos. 

Nota: Si se introduce el nombre de un alumno que ya existe el programa 
nos dará un error.

Ejercicio 5. Crea una tupla con los meses del año, pide números al usuario, 
si el número está entre 1 y la longitud máxima de la tupla, muestra el 
contenido de esa posición sino muestra un mensaje de error. 
El programa termina cuando el usuario introduce un cero.
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
    print('EJERCICIO 2: Ingreso de palabras')
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

    # Ejercicio 4
    class Alumno:

        __alumnos = []

        def __init__(self, nombre: str) -> None:
            self.nombre = nombre
            self.notas = []
            Alumno.__alumnos.append(self)

        def agregar_nota(self, nota: float):
            if nota < 0 or nota > 10:
                raise ValueError('nota debe estar dentro de rango [0, 10]')
            self.notas.append(nota)

        def get_media(self) -> float:
            return (sum(self.notas)/len(self.notas)) if len(self.notas) != 0 else 0

        @staticmethod
        def existe_alumno(nombre: str) -> bool:
            for a in Alumno.__alumnos:
                if a.nombre == nombre:
                    return True
            return False

        @staticmethod
        def listar_alumnos():
            alumnos = {x.nombre: x.get_media()
                       for x in Alumno.__alumnos}

            # recorremos diccionario
            for alumno, nota in alumnos.items():
                print('Alumno: %s\nPromedio: %.2f' % (alumno, nota))
                print('---')

    # ingreso de alumnos
    for i in range(int(input('Alumnos a ingresar: '))):
        nombre = input(f'nombre alumno {i+1}: ')

        # verifica existencia de alumno, si existe
        # rompe el programa
        if Alumno.existe_alumno(nombre):
            raise ValueError('Alumno ya se había ingresado')

        p = Alumno(nombre)

        # ingreso de calificaciones
        calif = 0
        while (calif >= 0):
            calif = float(input('Ingrese nota entre [0, 10]: '))
            if calif >= 0:
                p.agregar_nota(calif)

    # listamos alumnos con su respectivo promedio
    print('\n' + '-'*50)
    print('\nPromedio Alumnos:')
    Alumno.listar_alumnos()
    print('-'*50)
    
    # Ejecercicio 5
    print('EJERICIO 5. Muestra mes')
    meses = ('ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO',
             'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE')
    while True:
        n = int(input('Ingrese dia: '))
        match n:
            case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
                print(meses[n-1])
            case 0:
                print('Adiós!')
            case _:
                print('Error, opción inválida')

        # rompe el while
        if n == 0:
            break

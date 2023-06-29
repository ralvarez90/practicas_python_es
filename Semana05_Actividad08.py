# -*- coding: utf-8 -*-

"""ACTIVIDAD 08 - SEMANA 05

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 23-06-2023

Ejercicio 1. Escribe un programa Python que pida un número por teclado 
y que cree un diccionario cuyas claves sean desde el número 1 hasta el 
número indicado, y los valores sean los cuadrados de las claves.

Ejercicio 2. Escribe un programa que lea una cadena y devuelva un diccionario 
con la cantidad de apariciones de cada carácter en la cadena.

Ejercicio 3. Vamos a crear un programa en Python donde vamos a declarar 
un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido 
y nos mostrará el precio final de la fruta a partir de los datos guardados 
en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta 
el programa nos preguntará si queremos hacer otra consulta.
"""


# ejercicio 1
print('Ejercicio 1', '-'*20)
n = int(input('Ingrese entero > 1 : '))
assert isinstance(n, int) and n > 1
diccionario = {i: i**2 for i in range(1, n+1)}
print(diccionario, end='\n\n')

# ejercicio 2
print('Ejercicio 2', '-'*20)
palabra = input('Ingrese palabra: ')
dict_contador = {c: palabra.count(c) for c in palabra}
print(dict_contador, end='\n\n')

print('Ejercicio 3', '-'*20)
frutas = {
    'platano': 21.90,
    'manzana': 54.00,
    'limon': 34.90,
    'naranja': 29.90,
    'mango': 26.90,
    'pera': 44.90,
    'kiwi': 59.90,
}

nueva_consulta = True
while nueva_consulta:
    nombre_fruta = input('Fruta: ')
    if not nombre_fruta in frutas:
        print('Fruta no encontrada')
        continue

    cantidad_vendida = int(input('cantidad vendida (kg): '))

    if cantidad_vendida >= 0:
        print('Total: $%.2f' % (cantidad_vendida*frutas.get(nombre_fruta)))
    else:
        print('Error al ingresar cantidad vendida!')

    if input('Desea hacer otra consulta (si/no): ').lower() == 'si':
        continue
    else:
        nueva_consulta = False

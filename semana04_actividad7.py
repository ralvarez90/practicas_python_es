"""ACTIVIDAD 07 - SEMANA 04

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 00-06-2023


"""


# Ejercicio 1, función muestra el menu y retorna lo ingresado
def mostrar_menu():
    print('EJERCICIO 01\n' + ' MENU '.center(30, '-'))
    print('1. Primera opcion')
    print('2. Segunda opcion')
    print('3. Tercera opcion')
    print('0. Salir')
    return int(input('>>> '))


while True:
    entrada = mostrar_menu()
    match entrada:
        case 1 | 2 | 3:
            pass
        case 0:
            print('Adios!')
            break
        case _:
            print('Opcion Invalida!')


# Ejercicio 2, mostra los n primeros primos
def es_primo(n: int) -> bool:
    """Verifica si un entero es primo o no
    """
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


def primers_n_primos(n: int):
    """Retorna un generador de los primeros n primos
    """
    counter = 0
    primo = 1
    while counter < n:
        primo += 1
        if es_primo(primo):
            counter += 1
            yield primo


# ingrese entero
print('\nEJERCICIO 02')
n = int(input('Ingrese total de números primos a mostrar: '))
primos = primers_n_primos(n)
for p in primos:
    print(p, end=' ')
print()


print('\nEJERCICIO 03')
pagos = []
pago = 10
while len(pagos) != 20:
    pagos.append(pago)
    pago *= 2
print('Pagos:', pagos)
total_a_pagar = sum(pagos)
print('Totala pagar: $%d' % (total_a_pagar))

# Ejercicio 4. Calcular factorial
print('\nEJERCICIO 04')


def factorial(n: int) -> int:
    return 1 if n < 2 else n*factorial(n-1)


n = int(input('Ingrese entero > 2: '))
print(f'Factorial de {n} = {factorial(n)}')

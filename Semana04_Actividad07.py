"""ACTIVIDAD 07 - SEMANA 04

Nombre: José Rodrigo Álvarez Herrera
Folio : 406RD06
Fecha : 26-06-2023

PROGRAMACIÓN ORIENTADA A OBJETOS

Ejercicio 01. Crea una clase Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos
- Los setters y getters para cada uno de los atributos. Hay que validar entradas
- mostrar(): Muestre los datos de las personas
- esMayorDeEdad

Ejercicio 02. Crea una clase llamada Cuenta que tendrá los siguientes atributos: 
- titular  (que es una persona) 
- cantidad (puede tener decimales) 

El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos 
para la clase: 
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
  no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

Ejercicio 03.
Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase Cuenta Joven 
que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se 
debe guardar una bonificación que estará expresada en tanto por ciento. 
Construye los siguientes métodos para la clase:
- Un constructor.Los setters y getters para el nuevo atributo. En esta ocasión los titulares de 
  este tipo de cuenta tienen que ser mayor de edad; por lo tanto hay que crear un método es 
  TitularVálido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y 
  falso en caso contrario.
  Además la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

"""


class Persona:
    """Ejercicio 1.
    """

    def __init__(self, nombre: str = '', edad: int = 0, dni: str = 'empty') -> None:
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        assert edad >= 0
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni: str):
        assert len(dni) != 0
        self.__dni = dni

    def esMayorDeEdad(self) -> bool:
        return self.edad >= 18

    def __repr__(self) -> str:
        return 'Persona{nombre=%s, edad=%2d, dni=%s}' % (self.nombre, self.edad, self.dni)

    def mostrar(self):
        print(self)


class Cuenta:
    """Ejercicio 2
    """

    def __init__(self, titular: Persona, cantidad: float = 0.0) -> None:
        self.titular = titular
        self.cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular: Persona):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad: float):
        self.__cantidad = cantidad

    def ingresar(self, monto: float):
        if monto > 0:
            self.cantidad += monto

    def retirar(self, monto: float):
        self.cantidad -= monto

    def mostrar(self):
        print('Titular:', self.titular)
        print('Disponible: $%.2f' % (self.cantidad))


class CuentaJoven(Cuenta):
    """Ejercicio 03
    """

    def __init__(self, titular: Persona, cantidad: float = 0, bonificacion: int = 0) -> None:
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
        self.cantidad *= (1+self.bonificacion/100)

    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion: int):
        assert bonificacion >= 0 and bonificacion <= 100
        self.__bonificacion = bonificacion

    def titularValido(self) -> bool:
        return self.titular.edad >= 25

    def retirar(self, monto: float):
        if self.titularValido():
            super().retirar(monto)

    def mostrar(self):
        print('CUENTA JOVEN ---')
        return super().mostrar()


# ejemplo de pruena
if __name__ == '__main__':
    cuentaJoven = CuentaJoven(Persona('Rodrigo', 33, 'GV2'), 10000, 10)
    cuentaJoven.mostrar()

from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self,nombre='',apellido='',dni='',edad=0):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni        
        self.__edad = edad

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
    
    #GETTER nombre
    @property
    def nombre(self):
        return self.__nombre

    #SETTER nombre
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

    #GETTER apellido
    @property
    def apellido(self):
        return self.__apellido

    #SETTER apellido
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido = nuevo_apellido

    #GETTER dni
    @property
    def dni(self):
        return self.__dni

    #SETTER dni
    @dni.setter
    def dni(self,nuevo_dni):
        self.__dni = nuevo_dni

    #GETTER edad
    @property
    def edad(self):
        return self.__edad

    #SETTER edad
    @edad.setter
    def edad(self,nuevo_edad):
        self.__edad = nuevo_edad

    @abstractmethod
    def mostrar(self):
        pass
        #return f'Apellido: {self.apellido}, Nombre: {self.nombre}, DNI: {self.dni}, Edad: {self.edad}'  

    @abstractmethod
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False


class Cuenta(Persona):
    def __init__(self, nombre='', apellido='', dni='', edad=0, cantidad=0.0):
        super().__init__(nombre, apellido, dni, edad)
        self.__cantidad=cantidad

    #GETTER cantidad
    @property
    def cantidad(self):
        return self.__cantidad

    #SETTER nombre
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        self.__cantidad = nueva_cantidad

    @abstractmethod
    def mostrar(self):
        return f'Apellido: {self.apellido}, Nombre: {self.nombre}, DNI: {self.dni}, Edad: {self.edad}, Cantidad: {self.cantidad}'

    @abstractmethod
    def ingresar(self):
        deposito=float(input("Ingrese el monto a depositar: "))
        if deposito < 0:
            print("No se puede depositar montos negativos")
        else:
            nueva_cantidad= nueva_cantidad+deposito

    @abstractmethod
    def retirar(self):
        retiro=float(input("Ingrese el monto a retirar: "))
        nueva_cantidad= nueva_cantidad-retiro


class CuentaJoven(Cuenta):
    def __init__(self, nombre='', apellido='', dni='', edad=0, cantidad=0.0, bonificacion=0):
        super().__init__(nombre, apellido, dni, edad, cantidad)

    @abstractmethod
    def es_titular_valido(edad):
        if edad >= 18 and edad < 25:
            return True
        else:
            return False
        
    @abstractmethod
    def mostrar(self):
        return f'Cuenta Joven. Bonificacion de {self.bonificacion}%'
    
    @abstractmethod
    def retirar(self):
        if es_titular_valido(edad):
            return super().retirar()
        
ejemplo= Persona('Jorge', 'Stratta', '56778983', 56)
print(ejemplo.nombre)
        




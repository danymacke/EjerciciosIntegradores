from abc import ABC, abstractmethod


class Persona(ABC):

    def __init__(self,nombre='',apellido='',dni='',edad : int = 0):
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

   # @abstractmethod
   # def mostrar(self):
   #     pass
        #return f'Apellido: {self.apellido}, Nombre: {self.nombre}, DNI: {self.dni}, Edad: {self.edad}'  

    #@abstractmethod
    #def es_mayor_de_edad(self):
        #if self.edad >= 18:
        #    return True
        #else:
        #    return False
       # pass

class Cuenta(Persona):
    def __init__(self, nombre='', apellido='', dni='', edad=0, cantidad : float = 0):
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

    #@abstractmethod
    def mostrar(self):
        print(f'Apellido: {self.apellido}, Nombre: {self.nombre}, DNI: {self.dni}, Edad: {self.edad}, Saldo: {self.cantidad}')

    #@abstractmethod
    def ingresar(self, deposito:float = 0):
        deposito=float(input("Ingrese el monto a depositar: "))
        if deposito < 0:
            print("No se puede depositar montos negativos")
        else:
            self.cantidad= self.cantidad+deposito
            print(f"El nuevo saldo es de: {self.cantidad}")

    #@abstractmethod
    def retirar(self):
        retiro=float(input("Ingrese el monto a retirar: "))
        self.cantidad= self.cantidad-retiro
        print(f"El nuevo saldo de su cuenta es de: {self.cantidad}")


class CuentaJoven(Cuenta):
    def __init__(self, nombre='', apellido='', dni='', edad=0, cantidad : float = 0, bonif : float = 0):
        super().__init__(nombre, apellido, dni, edad, cantidad)
        self.__bonif= bonif

    #GETTER bonificacion
    @property
    def bonif(self):
        return self.__bonif

    #SETTER bonificacion
    @bonif.setter
    def bonif(self,nueva_bonif):
        self.__bonif = nueva_bonif

    #@abstractmethod
    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False
        
    #@abstractmethod
    def mostrar(self):
        print(f'Cuenta Joven. Bonificacion de {self.bonif}%')
        print(f'Apellido: {self.apellido}, Nombre: {self.nombre}, DNI: {self.dni}, Edad: {self.edad}, Saldo: {self.cantidad}')
    
    #@abstractmethod
    def retirar(self):
        if self.es_titular_valido():
            return super().retirar()
        else:
            print("Titular no valido para Cuenta Joven, imposible retirar.")
        
#ejemplo= Persona('Jorge', 'Stratta', '56778983', 56)
#print(ejemplo.nombre)
        
def tester():
    print('\n*****Ejemplo CUENTA JOVEN*****\n')
    ejemplo = CuentaJoven('Jose', 'Perez', '12345678', 23, 0, 5.7)
    #print(ejemplo.nombre)
    #print(ejemplo.bonif)
    ejemplo.mostrar()
    ejemplo.ingresar()
    ejemplo.retirar()
    
    print("\n*****Ejemplo CUENTA*******\n")
    ejemplo2 = Cuenta('Ana', 'Martinez', '16876098', 56, 900)
    ejemplo2.mostrar()
    ejemplo2.ingresar()
    ejemplo2.retirar()
    
tester()



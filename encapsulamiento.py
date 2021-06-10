"""
Ocultamiento de datos del estado interno para proteger la integridad del objeto
"""

class Cliente():
    def __init__(self, variable_publica, variable_encapsulada, variable_privada):

        self.variable_publica = variable_publica
        #un guion para protegido
        self._variable_encapsulada = variable_encapsulada
        # 2 guiones para privado
        self.__variable_privada = variable_privada

    def saludar(self):
        print("metodo publico " + str(self.__variable_privada))

    def __metodo_privado(self):
        print("Soy un metodo privado " + str(self.__variable_privada))

c = Cliente(1, 2, 3)


print(c.variable_publica)

#Accedemos a atributo protegido
print(c._variable_encapsulada)

# No permite acceder a variable privada
#print(c.__variable_privada)

#Manera correcta para acceder a variable privada
# objeto._clase__vairable
print(c._Cliente__variable_privada)

#Acceder a metodo privado
print(c._Cliente__metodo_privado())

c.saludar()
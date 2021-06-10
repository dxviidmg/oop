"""
Polimorfismo: Cuando un objeto cambia de forma y por ende de comportamiento
"""
class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")


class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")



def desplazamientoVehiculo(vehiculo):
    """
    Este metodo recibe un objeto y desde aqui llama al metodo de este,
    que en todos los metodos es el mismo nombre pero con conportamiento distinto
    """
    vehiculo.desplazamiento()



# Creación del objecto
mv = Camion()

# ejecución del polimofismo
desplazamientoVehiculo(mv)
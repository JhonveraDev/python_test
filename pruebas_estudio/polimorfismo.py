class Coche():
    def desplazamiento(self):
        print("4 Ruedas")
        
class Moto():
    def desplazamiento(self):
        print("2 Ruedas")

class Camion():
    def desplazamiento(self):
        print("6 Ruedas")
        
def desplazamiento(Vehiculo):
    Vehiculo.desplazamiento()        
        
        

moto=Moto()
desplazamiento(moto)    

carro=Coche()
desplazamiento(carro)     


        
        
        
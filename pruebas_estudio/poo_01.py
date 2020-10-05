class Coche():
    def __init__(self): #Estado inicial de la clase - Constructor
        
        self.__largo_chasis = 250 #Encapsulamiento
        self.__ruedas_chasis = 120 #propiedades
        self.__ruedas = 4
        self.marcha = False
   
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        
        if(self.enmarcha):
            chequeo = self.chequeo_interno()
        
        if(self.enmarcha and chequeo):
            return 'Vehiculo en movimiento'
        
        elif(self.enmarcha and chequeo==False):
            return 'Hay problemas en el chequeo, no se debe arrancar'
        
        else:
            return 'Vehiculo detenido'
        
        
    def estado(self):
        print("el vehiculo tiene ",self.__ruedas,"ruedas y un largo de chasis del: ", self.__largo_chasis)
    
    def chequeo_interno(self):
        self.gasolina='ok'
        self.aceite='agotado'
        self.puertas='cerradas'
        
        if(self.gasolina=='ok' and self.aceite=='ok' and self.puertas=='cerradas'):
            return True
        else:
            return False
        
    
        
mi_coche=Coche()
print(mi_coche.arrancar(True))
mi_coche.estado()

# otro_coche=Coche()
# # otro_coche.ruedas=55   Este tipo de errores no deben ocurrir, por eso se utiliza el encapsulamiento
# print(otro_coche.arrancar(False))
# otro_coche.estado()

            
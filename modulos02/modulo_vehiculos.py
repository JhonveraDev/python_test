class Vehiculo():
    
    def __init__(self,marca,modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False#Comportamientos iniciales
        self.acelera=False
        self.frena=False
        
    
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True #Comportamientos iniciales
        
    def frenar(self):
        self.frena=True    
        
    def estado(self):
        
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)    

class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"
        
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nse encuentra con carga: ",self.carga)     
                 

class Vehiculos_electricos():
    
    def __init__(self):
        self.marca=marca
        self.autonomia=100
 
        
    def energia(self,bateria):
        self.carga=bateria
        if(self.carga):
            return "Bateria Completa"
        else:
            return "Bateria vacia"

class Moto(Vehiculo): #Herencia
          
    def caballito(self):
        self.hcaballito="Montar en dos ruedas"
    
    hcaballito=''
    def estado(self): #Sobre escritura de metodos
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha ",self.enmarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nademas ",self.hcaballito)    
    

# mi_moto=Moto('Honda','CBR')
# mi_moto.arrancar()
# mi_moto.caballito()
# mi_moto.estado()  

# mi_furgoneta=Furgoneta("Hyn","ZXC")
# mi_furgoneta.arrancar()
# mi_furgoneta.acelerar()
# mi_furgoneta.carga(True) 
# mi_furgoneta.estado()  

# bici_electrica=Vehiculos_electricos("Tesla")
# print(bici_electrica.energia(True))


class Bici_electrica(Vehiculo,Vehiculos_electricos): #Herencias multiples
    pass

mi_bici=Bici_electrica("Tesla","2020")
mi_bici.estado()
    
                   
        
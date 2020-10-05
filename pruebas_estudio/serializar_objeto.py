import pickle

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):
        self.acelera=True
        
    def frenar(self):
        self.frena=True
        
    def estado(self):
        
        print("\nMarca: ",self.marca,"\nModelo",self.modelo,"\nEn marcha: ",self.enmarcha,"\nFrena:",self.frena)        

carro01=Vehiculo('Tesla','SBR')
carro02=Vehiculo('Kia','ZVB')
carro03=Vehiculo('Hyundai','DRD')

coches=[carro01,carro02,carro03]

fichero=open('los_coches','wb') #Escritura de informacion serializada en binario (Se guarda esta informacion siempre en el USSER de Windows)
pickle.dump(coches,fichero)

fichero.close()


fichero_apertura=open('los_coches','rb') #Apertura y lectura del fichero binario
mis_coches=pickle.load(fichero_apertura)
fichero_apertura.close()

for c in mis_coches: #Realiza la lectura por medio de un ciclo 
    print(c.estado())
 

       
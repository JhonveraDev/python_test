import pickle
import serializar_objeto 

fichero_apertura=open('los_coches','rb') #Apertura y lectura del fichero binario
mis_coches=pickle.load(fichero_apertura)
fichero_apertura.close()

for c in mis_coches: #Realiza la lectura por medio de un ciclo 
    print(c.estado())
 
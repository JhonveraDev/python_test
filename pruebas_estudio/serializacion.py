import pickle

# lista_nombres=['Pedro','Ana','Maria','Isa']

# fichero_binario = open("listas_nombre","wb")

# pickle.dump(lista_nombres,fichero_binario)

# fichero_binario.close()


fichero=open("listas_nombre","rb")

lista=pickle.load(fichero)
print(lista)


from io import open

archivo_texto=open("archivo.txt","w")

frase="Hola"
#En este caso se crea en el USSER del PC
archivo_texto.write(frase)

archivo_texto.close() #Cierra el archivo en memoria
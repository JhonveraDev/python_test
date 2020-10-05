listas=["01","02","03","04"] #Las cadenas puede guardar datos de tipo Bool, enteros, reales, flotantes o char
listas.append("06")
listas.insert(1,"300")
listas.extend(["800","900","1000"])



print(listas[0])
print(listas[2])
print(listas[0:3])
print(listas[:])
print(listas[0:3])
print(listas.index("800")) # Saber el index o posicion de un elemento
print("p" in listas) # para saber si es falso o verdadero 

listas.remove("1000")
print(listas[:])


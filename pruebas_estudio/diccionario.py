diccionario={"Alemania":"Berlin","Francia":"Paris","Colombia":"Bogota","España":"Madrid"}
diccionario["Italia"]="Lisboa"

print(diccionario["Francia"])
print(diccionario)
diccionario["Italia"]="Roma"
print(diccionario)

del diccionario["Francia"]
print(diccionario)

# Fusionar Tupla con Diccionario

Tupla=["Alemania","Colombia","Mexico","Canada"]
diccionarioFusion={Tupla[0]:"Berlin", Tupla[1]:"Bogotá", Tupla[2]:"Ciudad de mexico", Tupla[3]:"Ottawa"}

print(diccionarioFusion)
print(diccionarioFusion["Colombia"])

# La clave de un diccionario con varios elementos

DiccionarioPersonal={"Nombre":"Jhon","Edad":23, "Profesion": "Programador","Lenguajes":{"Principales":["Python","Java","C++","C#","React","Laravel"]}}
print(DiccionarioPersonal)

print(DiccionarioPersonal["Profesion"])
print(DiccionarioPersonal["Lenguajes"])
print(DiccionarioPersonal.keys())
print(DiccionarioPersonal.values())


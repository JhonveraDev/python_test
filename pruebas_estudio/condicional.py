print("Notas por consola")

Notas_Alumno=input("Nota del alumno")

def notes(Alumnos):
    resultado="Aprobado"
    
    if Alumnos < 5:
        resultado = "Suspendido"
    return resultado

print(notes(int(Notas_Alumno)))        
    
    
edad=int(input("Digita tu edad"))

def edades(edad_Alumno):
    
    if edad_Alumno < 18 and edad_Alumno > 0:
        fail= "menor de edad"
    

    elif edad_Alumno >= 18 and edad_Alumno <= 65:
        fail = "Mayor edad"
    
    elif edad_Alumno >=65 and edad_Alumno <= 99:    
        fail="Adulto Mayor"
    
    else:
        fail="Dato Incoherente"

    
    return fail            
      
        


  
print(edades(edad))     



#Estructura de listas por teclado

Nombre=input("escribe tu Nombre")
Direccion=input("Digita tu direccion")
Telefono=input("Tu numero de telefono")

listas=[Nombre,Direccion, Telefono]
print("Los datos personales son: " + listas[0]+ " " + listas[1]+ " " +listas[2])
    
        
    
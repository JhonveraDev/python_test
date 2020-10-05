import math
edad=int(input("Introducir tu edad por favor: "))

while edad<0 or edad > 100:

    if edad<0:
        print("Has introducido una edad negativa")
        edad=int(input("Digita nuevamente tu edad"))
        
    elif edad>99:
        print("Has introducido una edad alta")
        edad=int(input("Digita nuevamente tu edad"))        
        
print("Tu edad es correcta")       
        
        
 
#Modulo de prueba

print("Programa para evaluar raiz cuadrada")

digito=(int(input("Digita un numero positivo, solo tienes dos intentos: ")))  

contador=0

while digito<0:
    
    print("has digitado un numero negativo")
    contador=contador+1
    digito=(int(input("ingresa nuevamente un numero")))
    
    if contador == 1:
        print("has superado tu numero de intentos")
        print("Sesión finalizada")
        break;
    

if digito>0:
    while contador<2:
        contador=contador+1
        resultado=math.sqrt(digito)
        print("Resultado"+str(resultado))
        
        if contador<2:
            digito=(int(input("otr avez numero positivo: ")))  
        
        if digito<0:
            print("Ejecucion errada, Numero negativo")
            break;
 
    


    


    

       
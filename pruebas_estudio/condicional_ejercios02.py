# -*- coding: utf-8 -*-

#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# edad=int(input("Escribe tu edad"))

# if edad>18:
#     print("Mayor de edad")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# contraseña1="contraseña"
# contraseña2=input("Escribela nuevamente para comprobar")

# if contraseña1==contraseña2:
#     print("Coinciden las contraseñas")
    
# else:
#     print("No coincide")  

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

# numero01=int(input("Escribe un numero"))
# numero02=int(input("Escribe un numero"))

# if numero02==0:
#     print("Error, division no permitida")

# else:
#     operacion=numero01/numero02
#     print("Resultado "+str(operacion))    

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

# a=int(input("Digite un numero"))
# b=a%2

# if b == 0:
#     print("Numero Par")
# else:
#     print("numero Impar")    
    
#  Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.   
 
# edad=int(input("Digite su edad "))
# ingresos=int(input("Digite sus ingresos "))

# if edad >= 16 and ingresos >=1000:
#     print("debe tributar impuestos ")
    
# else:
#     print("No debe tributar impuestos ")    

# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# name = input("¿Cómo te llamas? ")
# gender = input("¿Cuál es tu sexo (M o H)? ")
# if gender == "M":
#     if name.lower() < "m":
#         group = "A"
#     else:
#         group = "B"
# else:
#     if name.lower() > "n":
#         group = "A"
#     else:
#         group = "B"
# print("Tu grupo es " + group)

# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# renta_anual= float(input("renta Anual")
#                    )
# if renta_anual < 10000:
#     print("Renta anual del 5%")

# elif renta_anual >= 10000 and renta_anual <= 20000:
#     print("Renta anual del 15%")

# elif renta_anual >= 35000 and renta_anual <= 200000:
#      print("Renta anual del 20%")
     
# elif renta_anual >= 60000 and renta_anual <= 350000:
#      print("Renta anual del 20%")     
     
#Ejercicio 8

# puntaje=float(input("Digita tu puntaje: "))


# if puntaje == 0.0:
#     print("Deficiente, no recibes comision")
            
# elif puntaje == 0.4:
#     comisionA=0.4*2400
#     print("Aceptable, tu comision es de: "+str(comisionA))      

# elif puntaje >= 0.6:
#     comisionB=0.6*2400
#     print("Excelente, tu comision es de: "+str(comisionB))    

# else:
#     print("puntajes no permitidos")

#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
    
    
# edad=int(input("¿Cual es su edad? "))
# if edad <=4:
#     print("La entrada es totalmente gratuita")
    
# elif edad >4 and edad <=18:
#     print("Costo de entrada: 5 Euros")    

# elif edad >18:
#     print("Costo de entrada: 10 Euros") 
                        
                        
#Ejercicio 10

def pizza(ingredientes):
    if ingredientes == 'vegetariana':
        print(f"Has elegido Pizza {ingredientes} ")
        contenido=input("Elige el ingrediente que deseas agregar pimiento o tofu ")
        contenidoCap=contenido.capitalize()
        print(f"Los ingredientes de tu pizza son: Mozarella,Tomate,{contenidoCap}")
        respuesta=input("¿ Es correcta su elección? ")
        respuestaCap=respuesta.upper()
        
        if respuestaCap == 'SI':
          
            print(f"Su respuesta ha sido {respuestaCap},Por favor espere 10 Minutos")
        
        elif respuestaCap == 'NO':
             print(f"Su respuesta ha sido {respuestaCap},Por favor Ingrese nuevamente su elección")
        else:
            print("Por favor ingresa una respuesta valida")     
        
        
    elif ingredientes == 'clasica':
        print(f"Has elegido Pizza {ingredientes} ")
        contenido=input("Elige el ingrediente que deseas agregar Jamón o Salmon ")
        contenidoCap=contenido.capitalize()
        print(f"Los ingredientes de tu pizza son: Mozarella,Tomate,{contenidoCap}")
        respuesta=input("¿ Es correcta su elección? ")
        respuestaCap=respuesta.upper()
        
        if respuestaCap == 'SI':
          
            print(f"Su respuesta ha sido {respuestaCap},Por favor espere 10 Minutos")
        
        elif respuestaCap == 'NO':
             print(f"Su respuesta ha sido {respuestaCap},Por favor Ingrese nuevamente su elección")
        else:
            print("Por favor ingresa una respuesta valida")
        
             
                       
    else:
        print("Por favor selecciona solo los ingredientes disponibles")


if __name__ == '__main__':
    print("Bienvenido a la PIZERIA NAPOLI")
    ingredientes=input("Por favor digita tu tipo de Pizza (Vegetariana ó Clasica)")
    ingredientes.lower()
    pizza(ingredientes)
                            
        


             





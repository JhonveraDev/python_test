# #Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra=input("Escribe una palabra")
# i=0
# while i<10:
#     i=i+1
#     print(palabra)

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# edad=int(input("Escribe tu edad"))
# i=0
# while i<edad:
#     i=i+1
#     print(i)

# #Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

# n = int(input("Introduce un número entero positivo: "))


# for i in range(1, n+1, 2):
#     print(i, end=", ")

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
# n = int(input("Introduce un número entero positivo: "))

# for i in range(n, -1, -1):
#     print(i, end=", ")


#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años?"))
# i=0

# while i<years:
#     i+=1

#     amount += interest / 100 
#     print("Capital tras " + str(i) + " años: " + str(round(amount, 2)))
    
    
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# valor=int(input("Digita numero entero positivo"))    

# for i in range(valor):
#     for j in range(i+1):
#         print("*",end="")
        
#     print(" ")   

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

# word = input("Introduce una palabra: ")
# space=len(word)
# i=0

# while i <space:
#     print(word[i])  
#     i+=1
    
# for i in range(len(word)-1, -1, -1):
#     print(word[i])    


#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
    
# frase = input("Introduce una frase: ")
# letra = input("Introduce una letra")
# contador = 0
# for i in frase:
#     if i == letra:
#         contador += 1
# print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
    
    

    
    
    
    




    
    
    
    
    


    
    
    
    


    
    
    





    
    


       
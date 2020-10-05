# #Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
# print("¡Hola Mundo!")

# #Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable
# dato= "¡Hola Mundo!"
# print(dato)

# #Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

# nombre_usser=input("Tu nombre ")
# print(f"Hola {nombre_usser}")

# #Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

# numero=int(input("Numero solicitado"))
# nombre=str(input("Nombre solicitado"))
# i=0

# while i<numero:
#     i=i+1
#     print(nombre)

#Escribir un programa que realice la siguiente operación aritmética  (3+22⋅5)

# resuelve = ((3+2)/(2*5))**2
# print(resuelve)

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde    

# horas_laborales=int(input("Digite sus horas laborales"))  
# dinero=int(input("Digite la cantidad de Dinero"))

# pago=horas_laborales*dinero

# print(f"Su pago es de {pago}")

#Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛. La suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente forma:
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales. 

# peso=float(input("Digita tu peso "))
# altura=float(input("Digita tu estatura "))    

# IMC= peso/(altura**2)   
# IMC=round(IMC,3)

# print(f"Tu IMC es de: {IMC}")

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

# n=int(input("Digita un numero "))
# m=int(input("Digita un numero "))

# c=n/m
# r=n%m

# print(f"El cociente es: {c} y el resto es {r}")

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

# cantidad=float(input("Cantidad a invertir por Mes "))
# interes_anual=float(input("Interes anual "))
# numero_años=int(input("Numero de años "))


# por_mes=cantidad*12
# porcentaje=(interes_anual * por_mes)/100
# capital= porcentaje*numero_años

# print(f"El retorno de la inversion en dinero es de:  {capital}")

#Ejercicio 13

# ahorros=float(input("Deposita tus ahorros "))
# porcentaje=(ahorros*4)/100
# segundo_año=((porcentaje*4)/100)+porcentaje
# tercer_año=(segundo_año*4)/100+porcentaje

# print("Primer año:"+str(round(porcentaje,2)))
# print("Segundo año: "+str(round(segundo_año,2)))  
# print("Tercer año: "+str(round(tercer_año,2)))    

#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

# barras_pan=int(input("Barras de pan vendidas del dia anterior "))

# barra_pan_fresco=3.49
# barra_pan_ayer=0.6
# barra_pan_descuento=(barras_pan*barra_pan_fresco)*barra_pan_ayer

# print("Valor de una barra de pan Fresco es de: " +str(barra_pan_fresco))
# print("La cantidad de barras de pan de ayer que vendiste fue de: " + str(barras_pan)+", con un descuento del 60%, y  por un valor total de: " +str(barra_pan_descuento))



                 
  
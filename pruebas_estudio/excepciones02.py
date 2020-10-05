import math

def calculaRaiz(num1):
    
    if num1<0:
        raise ValueError("El Numero no puede ser Negativo") 
    else:
        return math.sqrt(num1)
    
    
op1=(int(input("Digita un numero Positivo ")))  

try:
    print(calculaRaiz(op1)) 
    
except ValueError as ErrorNumeroNegativo:
    print(ErrorNumeroNegativo)
    
print("Programa finalizado")    
        
     

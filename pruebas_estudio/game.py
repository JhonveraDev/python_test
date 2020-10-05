import random

def run():
    numero_aleatorio=random.randint(1,10)
    numero_Usuario=int(input("Escribe un numero"))
    vidas=5
    i=1
    
    while numero_aleatorio != numero_Usuario:
        i=i+1
        if numero_Usuario < numero_aleatorio:
            numero_Usuario=int(input("Busca un numero mas grande, escribe nuevamente"))
        
        elif numero_Usuario > numero_aleatorio:
            numero_Usuario=int(input("Busca un numero mas pequeño, Escribe nuevamente"))
            
        if i==vidas:
            print(f"GAME OVER, EL NUMERO ES: {numero_aleatorio}")
            break   
                     
    
    if numero_aleatorio == numero_Usuario:
        print("Has adivinado el Numero") 
        print(f"El Numero aleatorio es: {numero_aleatorio}")   
       
    
        
if __name__ == '__main__':
    run()

        
def run():
    
    for contador in range(10):
        if contador % 2 != 0:
            continue
        print (contador)
    
    for i in range(10):
        
        print(i)
        if i== 7:
            break
    
    texto= input("Escribe Tu Nombre")
    
    for letra in texto:
        
        if letra=="o":
            print("Se encontro una o ")
            break
        print(letra)

if __name__ == '__main__':
    run()
    
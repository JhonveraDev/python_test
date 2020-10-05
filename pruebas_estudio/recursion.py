def facotiral(number):
    if number == 0:
        return 1
    return number * facotiral(number -1)
    
    


if __name__ == '__main__':
    number = int(input("Escribe un numero"))
    
    resultado = facotiral(number)
    
    print(resultado)   
def run():
    
    LIMITE = 25
    i = 1
    
    while i <=LIMITE:
        op= 2**i
        print(f"Posicion: {i}  se eleva a la 2 y su resultado es: {op} ")
        i=i+1
        
if __name__ == '__main__':
    run()
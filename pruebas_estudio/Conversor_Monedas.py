def exchanges(moneda,cantidad):
    result=0
    # Moneda Chilena
    if moneda == 1:
        result = cantidad * 0.0013
        Round= round(result,2)
        print(f"Los {cantidad} pesos chilenos equivales a: {Round} Doalres ")
    
    elif moneda == 2:
        result = cantidad * 0.00026
        Round= round(result,2)
        print(f"Los {cantidad} pesos Colombianos equivales a: {Round} Dolares ")
        
    elif moneda == 3:
        result = cantidad * 0.046  
        Round= round(result,2)
        print (f"Los {cantidad} pesos Mexicanos equivalen a: {Round} Dolares ")
        
    elif moneda == 4:
        result = cantidad * 0.014
        Round= round(result,2)
        print (f"La {cantidad} pesos Argentinos equivales a: {Round} dolares ") 
        
    else:
        print ("Por favor solo ingresa el valor Numerico")
          

if __name__ == '__main__':
    try:
        moneda = int(input('''
        Ingresa el indice de la moneda que quieres convertir a dolar:
        [1] Moneda Chilena a Dolar
        [2] Moneda Colombiana a Dolar
        [3] Moneda Mexicana a Dolar
        [4] Moneda Argentina a Dolar
        Seleciona '''))  
        print("***********************************")
        
        cantidad =  int(input("Ingresa la cantidad que quieres convertir: ")) 
        exchanges(moneda,cantidad)
    except:
        
        print("Por favor, Ingresa solo los valores numericos") 
        print("* * * * *E R R O R * * * * *")  

        
        
                       
                
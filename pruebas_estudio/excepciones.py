def divide():
    while True:
        try:
            
            
            op1=int(input("Digita el Primer Numero "))
            op2=int(input("Digita el Segundo Numero "))
            
            if op1>100:
                raise TypeError("No permite un numero mayor a 100") #Despues de ejecutarse este error, no se habrá más lectura de codigo
            
            val=op1/op2
            valround=round(val,3)
            print("La division es: "+str(valround))
            break
            
            
        except ValueError:
            print("Error de Caracteres, digita nuevamente un numero")  
        except ZeroDivisionError:
            print("Error de division por cero, digita nuevamente un numero") 
        
        except:
            print("Error completamente desconocido")  
            
        finally: #Se ejecutara siempre, sin importar nada
            print("Ejecucion finalizada")      
                
        
if __name__ == '__main__':
    divide()
            
            
            
            
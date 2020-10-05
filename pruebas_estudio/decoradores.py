def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        
        print("Se va a realizar una operacion simple")
        
        funcion_parametro()
        
        print("Calculo finalizado")
        
        
    return funcion_interior

@funcion_decoradora
def suma():
    print(5+4)
    
    
def resta():
    print (5-4)
    
    
if __name__ == '__main__':
    suma()
    resta()
        
            
            
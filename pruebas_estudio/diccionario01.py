def run():
    mi_Diccionario={
        'Llave1': 1,
        'Llave2': 2,
        'Llave3': 3,       
    }
    
    poblacion_paises={
        "Colombia": 44_432_555,
        "España": 5,
        "Brasil": 6
        }    
    
    
    print(poblacion_paises["Colombia"])
    
    for pais in poblacion_paises.keys():
        print(pais)
    
    for pais in poblacion_paises.values():
        print(pais) 
        
    for pais, poblacion in poblacion_paises.items():
        print(pais+ str(poblacion) )
               
    
if __name__=='__main__':
    run()
        
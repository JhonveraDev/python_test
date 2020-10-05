# import random

# def busqueda_lineal(lista,objetivo):
#     match=False
    
#     for elemento in lista:
        
#         if elemento==objetivo:
#             match=True
    
#     return match

# if __name__ == '__main__':
    
#     tamaño_lista=int(input("Tamaño de la lista"))
#     objetivo=int(input("Numero a buscar"))
    
    
#     lista=[random.randint(0,100) for i in range(tamaño_lista)]
#     encontrado= busqueda_lineal(lista,objetivo)
#     print(lista)
#     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') 
#     #Operador Ternario
    
import random
lista=[random.randint(0,100) for i in range (10)]
print (lista)

len(lista)
lista[9]            
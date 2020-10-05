import pickle

class Persona():
    def __init__(self,nombre,genero,edad):
    
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        
        print("Se ha creado una persona nueva con el nombre de: ",self.nombre)
        
        
    def __str__(self):
        return "{}{}{}".format(self.nombre,self.genero,self.edad)        
    
class lista_personas:
    personas=[]
    
    def __init__(self):
        lista_de_personas=open("fichero_externo",'ab')
        lista_de_personas.seek(0)#Cursor para la lectura de informacion
        
        try:
            self.personas=pickle.load(lista_de_personas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        
        finally:
            lista_de_personas.close()
            del(lista_de_personas)        
    
    def agregar_personas(self,p):
        self.personas.append(p)
        self.guardar_personas_fichero_externo()
        
    def mostar_personas(self):
        for p in self.personas:
            print(p)    
            
    def guardar_personas_fichero_externo(self):
        lista_personas=open('fichero_externo','wb')
        pickle.dump(self.personas,lista_personas)   
        lista_personas.close()
        del(lista_personas)     

# mi_lista=lista_personas()    
# p=Persona('Sandra','F',29)    
# mi_lista.agregar_personas(p)


# mi_lista=lista_personas()    
# p=Persona('Hombero','M',38)    
# mi_lista.agregar_personas(p)

# mi_lista=lista_personas()    
# p=Persona('Yone','M',23)    
# mi_lista.agregar_personas(p)

# mi_lista.mostar_personas()

mi_lista=lista_personas()
personas=personas('sandra','F',23)
mi_lista.agregar_personas(personas)
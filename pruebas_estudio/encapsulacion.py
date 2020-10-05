class Alumno:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        
        
    
    @property #es un decorador que funciona como un Getter
    def nombre_lista(self): 
        return self.apellido+' '+self.nombre 
    
    @nombre_lista.setter
    def nombre_lista(self,nombre_completo):
        self.nombre,self.apellido=nombre_completo.split(' ')
        
        
a=Alumno('ABC',"ASD")

print(a.nombre_lista)        
        
           
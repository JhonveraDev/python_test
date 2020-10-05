class Persona():
    def __init__(self,nombre, edad,residencia):
        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia
        
    def descripcion(self):
        print("\nNombre: ",self.nombre,"\nEdad: ",self.edad,"\nResidencia: ",self.residencia)
            
        
        
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)  #Hereda Constructor   
        
        self.salario=salario
        self.antiguedad=antiguedad
        
        
    def descripcion(self):
        super().descripcion()       #Hereda funcion
        
        print("\nSalario: ",self.salario,"\nAntiguedad",self.antiguedad)
        
        

# jhon=Empleado("7'000.000","5 Años","Jhon Anderson Vera",print(input("Edad:")),"Nueva Zelanda") 

jhon=Empleado("7'000.000","5 Años","Jhon Anderson Vera","23","Nueva Zelanda")
jhon.descripcion()       
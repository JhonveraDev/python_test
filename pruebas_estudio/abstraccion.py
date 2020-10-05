class Lavadora:
    
    def __init__(self):
        pass
    
    def lavar(self,temperatura="Caliente"):
        self._llenar_tanque_de_agua(temperatura)
        self._agregar_jabon()
        self._lavar()
        self._centrifugar()
        
    def _llenar_tanque_de_agua(self,temperatura):
        print(f"Llenando el tanque con agua {temperatura}")
        
    def _agregar_jabon(self):
        print("Agregando Jabon")            
    
    def _lavar(self):    
        print("LAVANDO")
        
    def _centrifugar(self):
        print("Centrifugando ropa")

if __name__ == '__main__':
    lavadora=Lavadora()
    lavadora.lavar()
    
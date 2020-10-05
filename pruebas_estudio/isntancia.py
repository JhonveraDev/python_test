class Coordenadas:
    
    def __init__(self,x,y):
        
        self.x=x
        self.y=y
        
    def distancia(self,otra_coordenada):
        
        x_diff=(self.x - otra_coordenada.x)**2
        y_diff=(self.y - otra_coordenada.y) **2    
        
        return (x_diff+y_diff)** 0.5    
        
    
if __name__ == '__main__':
        
    coordenada_1=Coordenadas(100,20)
    coordenada_2=Coordenadas(4,8)
    
    
    print(coordenada_1.distancia(coordenada_2))
    print(isinstance(5, Coordenadas))
    

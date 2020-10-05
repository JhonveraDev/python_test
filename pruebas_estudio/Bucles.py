
contador=0
a=input("Escribe tu correo")

for i in a:
    
    if(i=="@" or i=="p"):
       contador=contador+1

if contador==2:
    print("El correo electronico es correcto")
else:
    print("El correo no es correcto")
    
    
    

#Range    

for i in range(5):
    print(i)
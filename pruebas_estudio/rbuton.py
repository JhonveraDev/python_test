from tkinter import *


root=Tk()

varOpcion=IntVar()

def imprimir():
    #print(varOpcion.get())
    
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegido Masculino")
        
    else:
        etiqueta.config(text="Has elegido Femenino")
            
        

Label(root,text="Genero:").pack()

Radiobutton(root,text="Masculino",variable=varOpcion,value=1,command=imprimir).pack() #este tipo de RB son excluyentes (no permite mas de una opcion)
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()


root.mainloop()


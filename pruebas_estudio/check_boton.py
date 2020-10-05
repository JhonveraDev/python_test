from tkinter import *

root=Tk()

root.title("Selección de personaje")

peach=IntVar()
bow=IntVar()
mario=IntVar()


def opcion_personaje():
    opcion_escogida=""
    
    if(peach.get()==1):
        opcion_escogida+= "Peach"
        
    if(bow.get()==1):
        opcion_escogida+= "Bowsette" 
        
    if(mario.get()==1):
        opcion_escogida+= "Mario" 
        
    textoFinal.config(text=opcion_escogida)   
           
           
foto=PhotoImage(file="imagen_pri.gif")
Label(root, image=foto).pack()


frame=Frame(root)
frame.pack()

Label(frame,text="Elige al personaje", width=50).pack()


Checkbutton(frame,text='Bowsette',variable=bow,onvalue=1,offvalue=0,command=opcion_personaje).pack()
Checkbutton(frame,text='Mario',variable=mario,onvalue=1,offvalue=0,command=opcion_personaje).pack()
Checkbutton(frame,text='Peach',variable=peach,onvalue=1,offvalue=0,command=opcion_personaje).pack()


textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()


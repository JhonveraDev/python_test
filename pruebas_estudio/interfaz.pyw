from tkinter import *

raiz = Tk() #Clase

raiz.title("Ventana de Pruebas")
# raiz.iconbitmap('a.png')
raiz.geometry('950x500')
raiz.config(bg='black')
raiz.config(relief="sunken")


#Apartado de los Frames
mi_frame = Frame()
mi_frame.pack(fill='y', expand='True')
mi_frame.config(bg='red')
mi_frame.config(width = '650', height='350')
mi_frame.config(cursor='pirate')
# mi_frame.config(relief='groove') #Bordes

raiz.mainloop()#Este metodo o instruccion siempre debe estar en ultimo lugar

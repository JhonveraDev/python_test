from tkinter import *

raiz=Tk()  

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
minombre=StringVar()

cuadroTexto=Entry(miFrame,textvariable=minombre)
cuadroTexto.grid(row=0,column=1,pady=10,padx=10)#Grilla de elementos para tener mayor control en la interfaz ( row and column )
cuadroTexto.config(fg='red', justify='center' )
nombreLabel=Label(miFrame,text="Nombre: ")
nombreLabel.grid(row=0,column=0,sticky='w')

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,pady=10,padx=10)#
apellidoLabel=Label(miFrame,text="Apellido: ")
apellidoLabel.grid(row=1,column=0,sticky='w')

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,pady=10,padx=10)#
apellidoLabel=Label(miFrame,text="Ciudad de residencia: ")
apellidoLabel.grid(row=2,column=0,sticky='w')

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=4,column=1,pady=10,padx=10)#
cuadroPass.config(show='*')
Passlabel=Label(miFrame,text="Contraseña")
Passlabel.grid(row=4,column=0,sticky='w')

comentariosLabel=Label(miFrame,text="Comentarios")
comentariosLabel.grid(row=5,column=0,sticky='w')
texto_comentario=Text(miFrame, width=16,height=5)
texto_comentario.grid(row=5, column=1,pady=10)
scrollvert=Scrollbar(miFrame,command=texto_comentario.yview)
scrollvert.grid(row=5,column=2,sticky="nsew") #Adaptacion del scroll bar a su contenedor
texto_comentario.config(yscrollcommand=scrollvert.set)


def codigoBoton():
    minombre.set('Jhon')

botonEnvio=Button(raiz,text="Enviar", command=codigoBoton)
botonEnvio.pack()



raiz.mainloop()

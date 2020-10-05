from tkinter import*
raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()
operacion=''
resultado=0


#--------------PANTALLA--------------

numeroPantalla=StringVar()

pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background='black',fg="#03f943",justify="right")

#--------------PULSACION--------------


def numeroPulsado(num):
    global operacion

    
    if operacion != "":
        numeroPantalla.set(num)
        
        operacion=""
    
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
    

#--------------FUNCION SUMA--------------

def suma(num):
    global operacion
    global resultado
    
    resultado+=int(num)
    operacion='suma'
    
    numeroPantalla.set(resultado)
    
    
   

#--------------FILA 1--------------

boton7=Button(miFrame,text='7', width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text='8', width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text='9', width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botondiv=Button(miFrame,text='/', width=3)
botondiv.grid(row=2,column=4)

#--------------FILA 2--------------

boton4=Button(miFrame,text='4', width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text='5', width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text='6', width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonrest=Button(miFrame,text='-', width=3)
botonrest.grid(row=3,column=4)

#--------------FILA 3--------------

boton1=Button(miFrame,text='1', width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text='2', width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text='3', width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonmult=Button(miFrame,text='x', width=3)
botonmult.grid(row=4,column=4)

#--------------FILA 4--------------

boton0=Button(miFrame,text='0', width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonsum=Button(miFrame,text='+', width=3, command=lambda:suma())
botonsum.grid(row=5,column=4)
botoncoma=Button(miFrame,text=',', width=3, command=lambda:numeroPulsado(","))
botoncoma.grid(row=5,column=2)
botonigual=Button(miFrame,text='=', width=3)
botonigual.grid(row=5,column=3)

raiz.mainloop()

from tkinter import *

root=Tk()
imagen = PhotoImage(file="imagen_pri.gif")
Label(root, image=imagen, bd=0).pack()

root.mainloop()

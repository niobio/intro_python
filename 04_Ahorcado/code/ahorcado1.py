import Tkinter as tkinter

ancho = 365
alto = 200

def mostrar():
    print(letra.get())

ventana = tkinter.Tk()
ventana.title("Juego del ahorcado")

imagen = tkinter.PhotoImage(file = 'img/img1.png')
canvas = tkinter.Canvas(ventana, width=ancho, height=alto)
canvas.create_image(0,0,image=imagen,anchor=tkinter.NW)
canvas.pack()

texto = tkinter.Label(text = 'ESTO ES UNA PRUEBA', anchor=tkinter.NW)
texto.pack()

letra = tkinter.StringVar()
entry = tkinter.Entry(textvariable = letra)
entry.pack()

boton = tkinter.Button(text = 'ENTRAR', command = mostrar)
boton.pack()

ventana.mainloop()

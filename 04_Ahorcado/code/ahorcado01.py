import Tkinter

ancho = 365
alto = 200

def mostrar():
    print(letra.get())

ventana = tkinter.Tk()
ventana.title("Juego del ahorcado")
#ventana.minsize(ancho, alto)

imagen = tkinter.PhotoImage(file = 'img1.png')
canvas = tkinter.Canvas(ventana, width=ancho, height=alto)
canvas.create_image(0,0,image=imagen,anchor=tkinter.NW)
canvas.pack()

texto = tkinter.Label(text = 'ESTO ES UNA PRUEBA', anchor=tkinter.NW)
texto.pack()

entry = tkinter.Entry()
entry.pack()

boton = tkinter.Button(text = 'ENTRAR')
boton.pack()

ventana.mainloop()

import  tkinter

ancho = 300
alto = 200

ventana = tkinter.Tk()
ventana.title('Juego del ahorcado')

imagen = tkinter.PhotoImage(file = 'img7.png')
canvas = tkinter.Canvas(ventana, width=ancho, height=alto)
canvas.create_image(0,0,image=imagen,anchor=tkinter.NW)
canvas.pack()





ventana.mainloop()

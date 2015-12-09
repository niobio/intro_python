# coding: utf-8
try:
    import tkinter
except:
    import Tkinter as tkinter
    
import random

# Medidas de la ventana
ancho = 365
alto = 200


# Lista de palabras
listapalabras = 'loco palabra ahorcado perdido'.split()

def palabra_azar(listapalabras):
    '''Función que elige una palabra al azar de una lista de palabras'''
    indice = random.randint(0, len(listapalabras) - 1)
    palabra = listapalabras[indice]
    return palabra
'''
class MiCanvas(tkinter.Canvas):
    def actualiza(self, img):
        global newimg
        newimg = tkinter.PhotoImage(file = 'img/img2.png')
        self.itemconfigure(img,image=newimg)
'''

def actualizaTablero(img):
    global newimg        
    newimg = tkinter.PhotoImage(file = 'img/img2.png')
    canvas.itemconfigure(img,image=newimg) 
    
    
# main

# Crea la ventana
ventana = tkinter.Tk()
ventana.title("Juego del ahorcado")

# Crea la imagen
imagen = tkinter.PhotoImage(file = 'img/img1.png')
canvas = tkinter.Canvas(ventana, width=ancho, height=alto)
img = canvas.create_image(0,0,image=imagen,anchor=tkinter.NW)
canvas.pack()


texto = tkinter.Label(text = 'PALABRA', anchor=tkinter.NW)
texto.pack()

entry = tkinter.Entry()
entry.pack()

boton = tkinter.Button(text = 'Enviar', command = lambda i=img: actualizaTablero(i))
#boton = tkinter.Button(text = 'Enviar')
#boton.bind('<Button-1>', lambda: actualizaTablero(img))
boton.pack()

#canvas.actualiza(img)
#newimg = tkinter.PhotoImage(file = 'img/img2.png')
#actualizaTablero(img)


ventana.mainloop()

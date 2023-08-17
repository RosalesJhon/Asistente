import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk, ImageDraw, ImageOps

def procesar_info(nm):
    
    nomb = nm

    ventana = tk.Tk()
    ventana.geometry('{}x{}+{}+{}'.format(400, 400, 500, 100))
    ventana.resizable(0,0)
            
    ventana.title("Asistente")
    ventana.config(bg='#fcfcfc')

    image2 = Image.open("./descarga.jpg")
    image2 = image2.resize((120, 78))
    photo2 = ImageTk.PhotoImage(image2)
    img_label2 = tk.Label(ventana, image=photo2)
    img_label2.image = photo2
    img_label2.place(x=150, y=5)

    titulo = Label(text=f"Hola {nomb} ¿En qué puedo ayudarte?")
    titulo.place(x=50,y=130)
    titulo.config(bg='#fcfcfc')

    ventana.mainloop()
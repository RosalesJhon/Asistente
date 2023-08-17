import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk, ImageDraw, ImageOps

ventana = tk.Tk()
ventana.geometry('{}x{}+{}+{}'.format(400, 400, 500, 100))
ventana.resizable(0,0)
        
ventana.title("Asistente")
ventana.config(bg='#fcfcfc')

image2 = Image.open("./descarga.jpg")
image2 = image2.resize((120, 78))
photo2 = ImageTk.PhotoImage(image2)
img_label2 = tk.Label(ventana, image=photo2)
img_label2.image = photo2  # Evita que la imagen se borre automáticamente
img_label2.place(x=150, y=5)

titulo = Label(text="Hola {nm} en nque puedo ayudarte ?")
titulo.place(x=50,y=130)
titulo.config(bg='#fcfcfc')

nombres = Label(text="NOMBRES")
nombres.place(x=40,y=100)
nombres.config(bg='#fcfcfc')
entrada_nombre = tk.Entry(width=35,highlightbackground = "black", highlightcolor= "blue", highlightthickness=1,justify="center")
entrada_nombre.place(x=140,y=100)

ventana.mainloop()
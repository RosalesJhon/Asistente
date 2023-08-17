import tkinter as tk
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import sqlite3
from cryptography.fernet import Fernet

class Verificar:
    def __init__(self):
        self.datos = [
            {"ID":"admin","CONTRA":"1234"}
        ]
    
    def ventana_principal(self):
        ventana = tk.Tk()
        ventana.geometry('{}x{}+{}+{}'.format(400, 200, 750, 300))
        ventana.title("Verificar")
        ventana.resizable(0,0)
        ventana.config(bg='#fcfcfc')
        verif_label = tk.Label(text="Crear Cuenta",font=('Times',13))
        verif_label.config(bg='#fcfcfc')
        verif_label.place(x=100,y=20)

        image = Image.open("./descarga.jpg")
        image = image.resize((70, 68))
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(image=photo)
        img_label.place(x=10,y=0)

        image1 = Image.open("./descarga.jpg")
        image1 = image1.resize((70, 68))
        photo1 = ImageTk.PhotoImage(image1)
        img_label1 = tk.Label(image=photo1)
        img_label1.place(x=310,y=0)

        id_label = tk.Label(text="Name",font=('Times', 13))
        id_label.config(bg='#fcfcfc')
        id_label.place(x=50,y=70)
        pass_label = tk.Label(text="Password",font=('Times', 13))
        pass_label.config(bg='#fcfcfc')
        pass_label.place(x=50,y=100)

        id_usuario = tk.Entry(highlightbackground = "black", highlightcolor= "blue", highlightthickness=1,width=30,justify="center",font=('Times', 10))
        contrasena = tk.Entry(highlightbackground = "black", highlightcolor= "blue", highlightthickness=1,width=30, show="*",justify="center",font=('Times', 10))
        id_usuario.place(x=165,y=70)
        contrasena.place(x=165,y=100)
        
        ventana.mainloop()
verificador = Verificar()
verificador.ventana_principal()
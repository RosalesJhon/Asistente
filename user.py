import tkinter as tk
from PIL import ImageTk, Image

ventana = tk.Tk()
ventana.title("Crear cuenta")
ventana.geometry('{}x{}+{}+{}'.format(600, 350, 500, 100))
ventana.resizable(0,0)
ventana.config(bg='#fcfcfc')
        
image = Image.open("./images.png")
image = image.resize((250, 250))
photo = ImageTk.PhotoImage(image)
img_label = tk.Label(image=photo)
img_label.place(x=10,y=50)

titulo = tk.Label(text="Crear Cuenta",font=("Arial",15))
titulo.place(x=390,y=50)
titulo.config(bg="#fcfcfc")

nm_label =tk.Label(text="Nombres",font=("Arial",13))
nm_label.config(bg='#fcfcfc')
nm_label.place(x=320,y=100)

pass_label = tk.Label(text="Contraseña",font=('Times', 13))
pass_label.config(bg='#fcfcfc')
pass_label.place(x=320,y=170)

nm_entrada = tk.Entry(width=30,highlightbackground= "black",highlightcolor="Blue",highlightthickness=1,justify="center",font=("arial",10))
nm_entrada.place(x=320,y=135)

pwd_entrada = tk.Entry(width=35,highlightbackground = "black", highlightcolor= "blue", highlightthickness=1, show="*",justify="center",font=('Times', 10))
pwd_entrada.place(x=320,y=205)

ventana.mainloop()
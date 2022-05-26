import tkinter as tk  # python 3
from tkinter import font as tkfont
from turtle import title  # python 3
from PIL import Image, ImageTk
from network import Network
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL

titulo = "Acerca del Autor"

text_about = """Mi nombre es Luis Enrique Balboa Flores y soy estudiante de la Escuela militar
de ingeniería, de último año de Ingeniería de Sistemas. Este proyecto fue
realizado en Python, aplicando la arquitectura MovilNet para la identificación de
huellas. El proyecto se realizó para el Club Litoral, agradeciendo al Pro. Diego
Villena quien acepto la realización del proyecto su reconocida institución.
"""

class AcercaDeAutor(tk.Frame):
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # avoid garbage collection
    
    def place_image(self, path, base_width=300, x=0, y=0):
        image = Image.open(path)
        wpercent = (base_width / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        image = image.resize((base_width, hsize), Image.ANTIALIAS)
        image_copy = image.copy()
        image_tk = ImageTk.PhotoImage(image_copy)
        label_image = tk.Label(self, image=image_tk)
        label_image.image = image_tk
        label_image.place(x=x, y=y)
        
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        image = Image.open('image/fondo10.jpg')
        self.copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self, image=photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=tk.BOTH, expand=tk.YES)
        self.place_image(path='image/emi400px.png', x=775, y=85)
        self.place_image(path='image/autor.jpeg', base_width=150, x=50, y=50)
        
        tk.Label(
            self,
            text=titulo,
            font=("Arial", 15, "bold"),
            anchor="e",
            justify=tk.LEFT
        ).place(x=200, y=325)

        tk.Label(
            self,
            text=text_about,
            font=("Arial", 15),
            anchor="e",
            justify=tk.LEFT
        ).place(x=200, y=350)

        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='VOLVER',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: controller.show_frame("MainWindow")
        ).place(x=850, y=550)
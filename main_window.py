import tkinter as tk
from PIL import Image, ImageTk


class MainWindow(tk.Frame):
    def resize_image(self, event):
        new_width = event.width
        new_height = event.height
        image = self.copy_of_image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        self.label.config(image=photo)
        self.label.image = photo  # avoid garbage collection

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        image = Image.open('image/fondo10.jpg')
        self.copy_of_image = image.copy()
        photo = ImageTk.PhotoImage(image)
        self.label = tk.Label(self, image=photo)
        self.label.bind('<Configure>', self.resize_image)
        self.label.pack(fill=tk.BOTH, expand=tk.YES)

        # EMI FRAME
        imageEmi = Image.open("image/emi400px.png")
        basewidth = 300
        wpercent = (basewidth / float(imageEmi.size[0]))
        hsize = int((float(imageEmi.size[1]) * float(wpercent)))
        imageEmi = imageEmi.resize((basewidth, hsize), Image.ANTIALIAS)
        imageEmi_copy = imageEmi.copy()
        photoEmi = ImageTk.PhotoImage(imageEmi_copy)

        labelEmi = tk.Label(self, image=photoEmi)
        labelEmi.image = photoEmi
        labelEmi.place(x=775, y=85)

        # CARTA DERMATOGLIFIA
        tk.Button(
            self,
            highlightbackground='#FBFF00',
            text='Carta Dermatoglifica',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: self.controller.show_frame("ResultFrame")).place(x=30, y=30)

        # CAPTAR HUELLA
        tk.Button(
            self,
            highlightbackground='#08FE04',
            text='CAPTAR HUELLA',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: self.controller.show_frame("TakeHuella")
        ).place(x=850, y=30)

        # Acerca del autor
        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='ACERCA DEL AUTOR',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: self.controller.show_frame("AcercaDeAutor")).place(x=850, y=300)

        # Volver
        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='SALIR',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=self.controller.destroy
        ).place(x=850, y=550)

import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from PIL import Image, ImageTk


class TakeHuella(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # window configuration
        self.controller.geometry("997x561")
        self.controller.resizable(False, False)
        self.controller
        font = ("Arial", "12", "bold italic")
        tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        tk.Label(self, text="SISTEMA DE RECONOCIMENTO DE PATRONES DACTILARES", bg='#ebac00',
                 font=font).place(x=233, y=30)
        tk.Label(self, text="BASADO EN LA TEORIA DE DERMATOGLIFIOS, PARA DETERMINAR", bg='#ebac00',
                 font=font).place(x=196, y=60)
        tk.Label(self, text="LOS TALENTOS Y CAPACIDADES GENÉTICAS DE LOS DEPORTISTAS", bg='#ebac00',
                 font=font).place(x=189, y=90)

        # tk.LabelFrame(self, bg='black', height=350, width=997).place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=35)

        orange = "#EB5E00"
        sep = 40
        piv = 140 + 30
        x = 45
        y = lambda x: piv + (x * sep)
        tk.LabelFrame(self, bg=orange, height=319, width=325).place(x=30, y=140)
        tk.Label(self, text="Datos del Atleta", font=font, bg=orange).place(x=x, y=piv)
        tk.Label(self, text="Nombres:", font=font, bg=orange).place(x=x, y=y(1))
        tk.Label(self, text="Apellidos:", font=font, bg=orange).place(x=x, y=y(2))
        tk.Label(self, text="CI:", font=font, bg=orange).place(x=x, y=y(3))
        tk.Label(self, text="Fecha Nac:", font=font, bg=orange).place(x=x, y=y(4))
        tk.Label(self, text="Telefono:", font=font, bg=orange).place(x=x, y=y(5))
        tk.Label(self, text="Genero:", font=font, bg=orange).place(x=x, y=y(6))
        xEntry = 150
        name = tk.Entry(self, font=font)
        name.place(x=xEntry, y=y(1))
        last_name = tk.Entry(self, font=font)
        last_name.place(x=xEntry, y=y(2))
        ci = tk.Entry(self, font=font)
        ci.place(x=xEntry, y=y(3))
        fecha_nac = tk.Entry(self, font=font)
        fecha_nac.place(x=xEntry, y=y(4))
        telefono = tk.Entry(self, font=font)
        telefono.place(x=xEntry, y=y(5))
        genero = tk.Entry(self, font=font)
        genero.place(x=xEntry, y=y(6))

        btn_save = tk.Button(
            self, text="Guardar", font=font, width=20
        ).place(x=30, y=500)

        btn_volver = tk.Button(
            self,
            highlightbackground='#FFC638',
            text='Volver',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: controller.show_frame("MainWindow")
        ).place(x=750, y=500)

        imageEmi = Image.open("image/manos.jpg")
        baseHeight = 315
        wpercent = (baseHeight / float(imageEmi.size[1]))
        wsize = int((float(imageEmi.size[0]) * float(wpercent)))
        imageEmi = imageEmi.resize((wsize, baseHeight), Image.ANTIALIAS)
        imageEmi_copy = imageEmi.copy()
        photoEmi = ImageTk.PhotoImage(imageEmi_copy)

        labelEmi = tk.Label(self, image=photoEmi)
        labelEmi.image = photoEmi
        labelEmi.place(x=360, y=140)
        """ finger buttons"""
        self.pulgar_i: tk.Button = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.pulgar_i))
        self.pulgar_i.place(x=368, y=283)
        self.indice_i = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.indice_i))
        self.indice_i.place(x=459, y=160)
        self.medio_i = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.medio_i))
        self.medio_i.place(x=508, y=148)
        self.anular_i = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.anular_i))
        self.anular_i.place(x=560, y=164)
        self.menhique_i = tk.Button(self, width=3, bg='green', command=lambda: self.openNewWindow(self.menhique_i))
        self.menhique_i.place(x=604, y=220)

    def open_app(self):
        import os
        # only works for windows
        os.startfile("{}\main.exe".format(os.getcwd()))

    def set_btn_valid(self, button):
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(filename)
        button.configure(bg='red')

    def openNewWindow(self, btn):
        newWindow = tk.Toplevel(self)
        newWindow.title("Captura de Huella Digital")
        newWindow.geometry("200x200")

        imageEmi = Image.open("image/fondo1.jpg")
        baseHeight = 200
        wpercent = (baseHeight / float(imageEmi.size[1]))
        wsize = int((float(imageEmi.size[0]) * float(wpercent)))
        imageEmi = imageEmi.resize((wsize, baseHeight), Image.ANTIALIAS)
        imageEmi_copy = imageEmi.copy()
        photoEmi = ImageTk.PhotoImage(imageEmi_copy)
        bg = tk.Label(newWindow, image=photoEmi)
        bg.image = photoEmi
        bg.place(x=0, y=0)

        tk.Button(newWindow, text="Capturar Huella", command=self.open_app).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        tk.Button(newWindow, text="Aceptar y Continuar", command=lambda: self.set_btn_valid(btn)).place(relx=0.5,
                                                                                                        rely=0.7,
                                                                                                        anchor=tk.CENTER)

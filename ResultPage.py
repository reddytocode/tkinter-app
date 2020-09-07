import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from PIL import Image, ImageTk
from network import Network
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL
from CurrentUserPersistance import get_user, Dedo, User


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        font = ("Arial", "12", "bold italic")
        self.current_user: User = get_user()

        tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        btn_volver = tk.Button(
            self,
            highlightbackground='#FFC638',
            text='Volver',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: controller.show_frame("MainWindow")
        ).place(x=750, y=500)
        if isinstance(self.current_user, User):
            tk.Label(self, text="RESUMEN DE CARACTERISTICAS", font=font).place(x=100, y=100)
            tk.Label(self, text="Nombres y Apellidos:   {} {}".format(self.current_user.name, self.current_user.lastName), font=font).place(x=100, y=200)
            tk.Label(self, text="ESTUDIO DE DERMATOGLIFOS", font=font).place(x=100, y=300)
            tk.Label(self, text="ARCOS:          {}".format(self.current_user.categ["arco"]), font=font).place(x=100, y=400)
            tk.Label(self, text="PRESILLAS:      {}".format(self.current_user.categ["presilla"]), font=font).place(x=100, y=500)
            tk.Label(self, text="VERTICILOS:     {}".format(self.current_user.categ["verticilo"]), font=font).place(x=100, y=600)
            tk.Label(self, text="D10:            {}".format(self.current_user.d10), font=font).place(x=100, y=700)
            tk.Label(self, text="SQTL:           {}".format(self.current_user.sqtl), font=font).place(x=100, y=800)
            # tk.Label(self, text="Nombres y Apellidos:   {} {}".format(self.current_user.name, self.current_user.lastName), font=font).place(100, 200)



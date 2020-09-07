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
        imageEmi = Image.open("image/fondopista.jpg")
        basewidth = 997
        style_ORANGE = {"bg": '#EB5E00', "font": font}
        wpercent = (basewidth / float(imageEmi.size[0]))
        hsize = int((float(imageEmi.size[1]) * float(wpercent)))
        imageEmi = imageEmi.resize((basewidth, hsize), Image.ANTIALIAS)
        imageEmi_copy = imageEmi.copy()
        photoEmi = ImageTk.PhotoImage(imageEmi_copy)

        labelEmi = tk.Label(self, image=photoEmi)
        labelEmi.image = photoEmi
        labelEmi.place(x=0, y=0)

        # users = Network.get_all()
        users = [User(), User()]
        names = ["{} - {}".format(index, user.name) for index, user  in enumerate(users)]

        # tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        tkvar = tk.StringVar(self)
        choices = names
        tkvar.set('')
        popupMenu = tk.OptionMenu(self, tkvar, *choices)

        tk.Label(self, text="Elija el usuario a mostrar", bg='#ebac00', font=font).place(x=10, y = 10)
        popupMenu.place(x=10, y=35)
        tk.Label(self, text="RESUMEN CARACTERISTICAS", **style_ORANGE).place(x=400, y=10)


        self.current_user = None
        def change_dropdown(*args):
            global genero_aux
            genero_aux = tkvar.get().split(' - ')
            index = genero_aux[0]
            self.current_user = users[int(index)]
            self.setUserTable()
            print("chooosen", index)

        tkvar.trace('w', change_dropdown)


        # self.current_user: User = get_user()
        #

        btn_volver = tk.Button(
            self,
            highlightbackground='#FFC638',
            text='Volver',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: controller.show_frame("MainWindow")
        ).place(x=750, y=500)
        # if isinstance(self.current_user, User):



    def setUserTable(self):
        font = ("Arial", "12", "bold italic")

        if(self.current_user is not None):
            style = {"bg": '#ebac00', "font": font}
            style_ORANGE = {"bg": '#EB5E00', "font": font}
            tk.Label(self, text="Nombres y Apellidos:   {} {}".format(self.current_user.name, self.current_user.lastName), **style).place(x=100, y=150)

            tk.Label(self, text="ESTUDIO DE DERMATOGLIFOS", **style).place(x=600, y=150)
            tk.Label(self, text="ARCOS:          {}".format(self.current_user.categ["arco"]), **style).place(x=600, y=200)
            tk.Label(self, text="PRESILLAS:      {}".format(self.current_user.categ["presilla"]), **style).place(x=600, y=225)
            tk.Label(self, text="VERTICILOS:     {}".format(self.current_user.categ["verticilo"]), **style).place(x=600, y=250)
            tk.Label(self, text="D10:            {}".format(self.current_user.d10), **style).place(x=750, y=200)
            tk.Label(self, text="SQTL:           {}".format(self.current_user.sqtl), **style).place(x=750, y=225)

            tk.Label(self, text="PREDOMINIO DE LAS CAPACIDADES DEPORTIVAS", **style_ORANGE).place(x=100, y=300)
            tk.Label(self, text="{} - \"{}\"".format(self.current_user.res_primer_analisis, self.current_user.formula_digital), **style).place(x=100, y=325)

            tk.Label(self, text="SE RECOMIENDA QUE TIENE APTITUDES PARA:", **style_ORANGE).place(x=100, y=450)
            try:
                tk.Label(self, text="Recomendacion 1:{}".format(self.current_user.recomendacion1["deporte"]), **style).place(x=100, y=475)
            except Exception as e:
                tk.Label(self, text="Recomendacion 1: No hay recomendacion", **style).place(x=100, y=475)

            try:
                tk.Label(self, text="Recomendacion 2:{}".format(self.current_user.recomendacion2["deporte"]), **style).place(x=100, y=500)
            except Exception as e:
                tk.Label(self, text="Recomendacion 2: No hay recomendacion", **style).place(x=100, y=500)


import tkinter as tk  # python 3
from tkinter import font  as tkfont  # python 3
from PIL import Image, ImageTk
from network import Network
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL


class Dedo:
    def __init__(self):
        self.category = None
        self.distance = 0
        self.huella_b64 = ""

    def is_valid(self):
        valid = self.category is not None
        print("valid", self.category, "id", valid)
        return valid

class User:
    def __init__(self):
        self.age = None
        self.name = None
        self.lastName = None
        self.ci = None
        self.fechaNac = None
        self.telf = None
        self.genero = None
        # dedos
        self.pulgar_i = Dedo()
        self.anular_i = Dedo()
        self.medio_i = Dedo()
        self.indice_i = Dedo()
        self.menhique_i = Dedo()
        self.res_primer_analisis = None
        self.formula_digital = None

    def print(self):
        print(self.name, "pulgar es:", self.pulgar_i.category)

    def primer_analisis(self):
        dedos = [self.pulgar_i, self.anular_i, self.medio_i, self.indice_i, self.menhique_i]
        res = {"arco": 0, "presilla": 0, "verticilo": 0}
        """
        arco => 1        (A)
        presilla => 2o 3 (L)
        verticillo => 4  (W)
        """
        for dedo in dedos:
            res[dedo.category] += 1
        A = res["arco"]
        L = res["presilla"]
        W = res["verticilo"]

        if(A == 10):
            self.res_primer_analisis = "FUERZA MAXIMA(no incluye potencia)"
            self.formula_digital = "10A"
        if(L >= 6 and W > 0 and A == 0):
            self.res_primer_analisis = "Velocidad, Potencia con un componente de resistencia y coordinacion"
            self.formula_digital = "LW"
        elif(W >=5 and L > 0 and A == 0):
            self.res_primer_analisis = "Resistencia y Coordinacion de Velocidad y Potencia"
            self.formula_digital = "WL"
        elif(A > 0 and L > 0 and W == 0):
            self.res_primer_analisis = "FUERZA MAXIMA, VELOCIDAD Y POTENCIA"
            self.formula_digital = "AL"
        elif(A > 0 and L > 0 and W > 0):
            # OJO PREGUNTAR
            self.res_primer_analisis = "Depende de la mayor proporcion"
            self.formula_digital = "ALW"
        elif(L == 10):
            self.res_primer_analisis = "POTENCIA Y VELOCIDAD"
            self.formula_digital = "10L"
        elif(W == 10):
            self.res_primer_analisis = "RESISTENCIA Y COORDINACION"
            self.formula_digital = "10W"







class TakeHuella(tk.Frame):

    def save(self):
        def check(field):
            if field is None or len(field) < 2:
                tk.messagebox.showerror(title="Formulario incompleto", message="Formulario incompleto")

        self.current_user.name = self.name.get()
        self.current_user.lastName = self.last_name.get()
        self.current_user.ci = self.ci.get()
        self.current_user.fechaNac = self.fecha_nac.get()
        self.current_user.telf = self.telefono.get()
        self.current_user.genero = self.genero.get()
        check(self.current_user.name)
        check(self.current_user.lastName)
        check(self.current_user.ci)
        check(self.current_user.fechaNac)
        check(self.current_user.telf)
        check(self.current_user.genero)
        if self.current_user.pulgar_i.is_valid() and self.current_user.indice_i.is_valid() and self.current_user.anular_i.is_valid() and self.current_user.medio_i.is_valid() and self.current_user.menhique_i.is_valid():
            # macke analysis
            pass
        else:
            tk.messagebox.showerror(title="Formulario incompleto", message="No se ingresaron todas las huellas")

    def __init__(self, parent, controller):
        self.current_user = User()
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
        self.name = tk.Entry(self, font=font)
        self.name.place(x=xEntry, y=y(1))
        self.last_name = tk.Entry(self, font=font)
        self.last_name.place(x=xEntry, y=y(2))
        self.ci = tk.Entry(self, font=font)
        self.ci.place(x=xEntry, y=y(3))
        self.fecha_nac = tk.Entry(self, font=font)
        self.fecha_nac.place(x=xEntry, y=y(4))
        self.telefono = tk.Entry(self, font=font)
        self.telefono.place(x=xEntry, y=y(5))
        self.genero = tk.Entry(self, font=font)
        tkvar = tk.StringVar(self)
        choices = {'Hombre', 'Mujer'}
        tkvar.set('Hombre')
        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        popupMenu.place(x=xEntry, y=y(6))

        def change_dropdown(*args):
            print(tkvar.get())

        tkvar.trace('w', change_dropdown)
        # self.genero.place(x=xEntry, y=y(6))

        btn_save = tk.Button(
            self, text="Guardar", font=font, width=20, command=self.save
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
        self.pulgar_i: tk.Button = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.pulgar_i,
                                                                                               self.current_user.pulgar_i))
        self.pulgar_i.place(x=368, y=283)
        self.indice_i = tk.Button(self, width=3,
                                  command=lambda: self.openNewWindow(self.indice_i, self.current_user.indice_i))
        self.indice_i.place(x=459, y=160)
        self.medio_i = tk.Button(self, width=3,
                                 command=lambda: self.openNewWindow(self.medio_i, self.current_user.medio_i))
        self.medio_i.place(x=508, y=148)
        self.anular_i = tk.Button(self, width=3,
                                  command=lambda: self.openNewWindow(self.anular_i, self.current_user.anular_i))
        self.anular_i.place(x=560, y=164)
        self.menhique_i = tk.Button(self, width=3,
                                    command=lambda: self.openNewWindow(self.menhique_i, self.current_user.menhique_i))
        self.menhique_i.place(x=604, y=220)
        # Being changed with is loading funtction
        self.progress = tk.Label(self, text="Cargando ... ...", font=font)

    def setIsLoading(self, isLoading):
        if isLoading:
            # your other label or button or ...
            self.progress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            self.progress.place_forget()

    def open_app(self):
        import os
        # only works for windows
        os.startfile("{}\main.exe".format(os.getcwd()))

    def set_btn_valid(self, button, newWindow, field: Dedo):
        self.setIsLoading(True)
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
        print(filename)
        print("making the request...")

        category = Network.get_category(filename)
        category = str(category)[2:-1]
        field.category = category
        if (category != "arco"):
            distance, encoded = Network.get_analisis_results(filename)
            if distance is None or encoded is None:
                tk.messagebox.showerror("Registro Huella",
                                        "No se encontro puntos caracteristicos en la huella, se la tomara de igual forma")
            field.huella_b64 = encoded
            field.distance = distance
        self.setIsLoading(False)
        if category is not None:
            tk.messagebox.showinfo("Registro Huella", "La huella de tipo {} ha sido registrada".format(category))
            button.configure(bg='green')
        else:
            tk.messagebox.showerror("Registro Huella", "La huella no ha sido registrada")
            button.configure(bg='red')

        # w = tk.Message(self, text="this is a relatively long message", width=50).pack()

        newWindow.destroy()

    def openNewWindow(self, btn, field):
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
        tk.Button(newWindow, text="Aceptar y Continuar",
                  command=lambda: self.set_btn_valid(btn, newWindow, field)).place(
            relx=0.5,
            rely=0.7,
            anchor=tk.CENTER)

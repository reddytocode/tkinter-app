from datetime import datetime
import tkinter as tk  # python 3

from PIL import Image, ImageTk

from CurrentUserPersistance import User, Dedo
from network import Network
from const import filename

genero_aux = "Hombre"


def validate_name(name):
    name_split = name.split(" ")
    try:
        if name[-1] == " ":
            if name[-2] == " ":
                return False
            return True
    except IndexError:
        return True

    for name_part in name_split:
        if not name_part.isalpha():
            return False
    return True


def validate_phone_number(telf):
    if len(telf) == 0:
        return True
    if len(telf) > 8:
        return False
    if len(telf) > 0:
        if " " in telf:
            return False
    try:
        if len(telf) == 1:
            return int(telf[0]) in (6, 7, 2)
        if telf.isdigit():
            return True
        int(telf)
        return True
    except ValueError:
        return False


class TakeHuella(tk.Frame):

    def save(self):
        global genero_aux

        def check(field):
            return field is None or len(field) < 2

        self.current_user.name = self.name.get()
        self.current_user.lastName = self.last_name.get()
        self.current_user.ci = self.ci.get()
        self.current_user.fechaNac = self.text.get()
        self.current_user.telf = self.telefono.get()
        self.current_user.genero = genero_aux
        fields_checker = [
            check(self.current_user.name),
            check(self.current_user.lastName),
            check(self.current_user.ci),
            check(self.current_user.fechaNac),
            check(self.current_user.telf),
            check(self.current_user.genero)
        ]
        if any(fields_checker):
            tk.messagebox.showerror(
                title="Formulario incompleto",
                message="Formulario incompleto"
                )
            return

        # self.controller.show_frame("ResultFrame")
        if self.current_user.pulgar_i.is_valid() and self.current_user.indice_i.is_valid() and self.current_user.anular_i.is_valid() and self.current_user.medio_i.is_valid() and self.current_user.menhique_i.is_valid() and self.current_user.pulgar_d.is_valid() and self.current_user.indice_d.is_valid() and self.current_user.anular_d.is_valid() and self.current_user.medio_d.is_valid() and self.current_user.menhique_d.is_valid():
            # macke analysis
            self.current_user.primer_analisis()
            self.current_user.calculate_d10()
            self.current_user.calculate_sqtl()
            recomendacion1, recomendacion2 = User.search_in_table(
                self.current_user.d10, self.current_user.tabla)
            # self.current_user.segundo_analisis()
            self.current_user.recomendacion1 = recomendacion1
            self.current_user.recomendacion2 = recomendacion2
            Network.saveUser(self.current_user)
            self.resultsWindow()
        else:
            tk.messagebox.showerror(
                title="Formulario incompleto", message="No se ingresaron todas las huellas")

    def print_sel(self):
        date = self.cal.selection_get()
        date = date.strftime("%Y-%m-%d")
        self.text.set(date)
        self.fecha_nac_label.place(
            x=self.fecha_nac_label_x, y=self.fecha_nac_label_y)
        self.fecha_btn.place_forget()
        self.top.destroy()

    def fecha_nac(self):
        from tkcalendar import Calendar
        # tkinter frame
        self.top = tk.Toplevel(self)
        self.cal = Calendar(self.top,
                    font="Arial 14", selectmode='day',
                            year=2000, month=1, day=1, locale="es", maxdate=datetime.now())
        self.cal.pack(fill="both", expand=True)
        tk.Button(self.top, text="ok", command=self.print_sel).pack()
    
    def __init__(self, parent, controller):
        print("init huella")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # window configuration
        self.controller.geometry("997x561")
        self.controller.resizable(False, False)
        self.refresh()

    def tkraise(self, aboveThis=None):
        self.refresh()
        return super(TakeHuella, self).tkraise()

    def refresh(self):
        self.current_user = User()
        font = ("Arial", "12", "bold")
        tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        # SISTEMAS DE RECONOCIMIENTO DE PATRONES DACTILARES 
        # BASADO EN LA TEORÍA DE DERMATOGLIFOS, PARA DETERMINAR LOS TALENTOS Y CAPASIDADES GENÉTICAS DE LOS DEPORTISTAS

        tk.Label(
            self,
            text="SISTEMA DE RECONOCIMENTO DE PATRONES DACTILARES",
            bg='#ebac00',
            anchor="center",
            font=font
        ).place(x=333, y=30)
        
        tk.Label(
            self,
            text="BASADO EN LA TEORÍA DE DERMATOGLIFIOS, PARA DETERMINAR",
            bg='#ebac00',
            anchor="center",
            font=font
        ).place(x=296, y=60)

        tk.Label(
            self,
            text="LOS TALENTOS Y CAPACIDADES GENÉTICAS DE LOS DEPORTISTAS",
            bg='#ebac00',
            anchor="center",
            font=font
        ).place(x=289, y=90)


        orange = "#EB5E00"
        sep = 40
        piv = 140 + 30
        x = 45
        def y(x): return piv + (x * sep)
        tk.LabelFrame(self, bg=orange, height=319,
                      width=325).place(x=30, y=140)
        tk.Label(self, text="Datos del Atleta",
                 font=font, bg=orange).place(x=x, y=piv)
        tk.Label(self, text="Nombre(s):", font=font,
                 bg=orange).place(x=x, y=y(1))
        tk.Label(self, text="Apellidos:", font=font,
                 bg=orange).place(x=x, y=y(2))
        tk.Label(self, text="CI:", font=font, bg=orange).place(x=x, y=y(3))
        tk.Label(self, text="Teléfono:", font=font,
                 bg=orange).place(x=x, y=y(4))

        tk.Label(self, text="Genero:", font=font, bg=orange).place(x=x, y=y(5))
        xEntry = 150
        self.xEntry = xEntry
        
        tk.Label(self, text="Fecha Nac:", font=font, bg=orange).place(x=x, y=y(6))
        
        reg = self.register(validate_name) 
        self.name = tk.Entry(self, font=font)
        self.name.config(validate="key", validatecommand=(reg, "%P"))

        self.name.place(x=xEntry, y=y(1))
        self.last_name = tk.Entry(self, font=font)
        self.last_name.config(validate="key", validatecommand=(reg, "%P"))

        self.last_name.place(x=xEntry, y=y(2))
        self.ci = tk.Entry(self, font=font)
        self.ci.place(x=xEntry, y=y(3))
        reg_telf = self.register(validate_phone_number)
        self.telefono = tk.Entry(self, font=font)
        self.telefono.config(validate="key", validatecommand=(reg_telf, "%P"))

        self.telefono.place(x=xEntry, y=y(4))
        self.genero = tk.Entry(self, font=font)
        
        self.fecha_btn = tk.Button(self, text="Fecha", 
                            command=self.fecha_nac,
                            font=font,
                            bg=orange)
        self.fecha_btn.place(x=xEntry, y=y(6))
        self.text = tk.StringVar()
        self.text.set("")
        self.fecha_nac_label = tk.Label(self, textvariable=self.text, font=font, bg=orange)
        self.fecha_nac_label_x = xEntry
        self.fecha_nac_label_y = y(6)
        
        tkvar = tk.StringVar(self)
        choices = {'Hombre', 'Mujer'}
        tkvar.set('Hombre')
        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        popupMenu.place(x=xEntry, y=y(5))

        def change_dropdown(*args):
            global genero_aux
            genero_aux = tkvar.get()

        tkvar.trace('w', change_dropdown)
        # self.genero.place(x=xEntry, y=y(6))

        tk.Button(
            self,
            text="GUARDAR",
            font=font,
            width=20,
            command=self.save
        ).place(x=30, y=550)

        def volver(self):
            self.refresh()
            self.controller.show_frame("MainWindow")
        
        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='VOLVER',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: volver(self)
        ).place(x=850, y=550)

        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='REFRESCAR',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: self.refresh()
        ).place(x=600, y=550)

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

        """ derecha"""
        self.pulgar_d: tk.Button = tk.Button(self, width=3, command=lambda: self.openNewWindow(self.pulgar_d,
                                                                                               self.current_user.pulgar_d))
        self.pulgar_d.place(x=875, y=323)
        self.indice_d = tk.Button(self, width=3,
                                  command=lambda: self.openNewWindow(self.indice_d, self.current_user.indice_d))
        self.indice_d.place(x=810, y=170)
        self.medio_d = tk.Button(self, width=3,
                                 command=lambda: self.openNewWindow(self.medio_d, self.current_user.medio_d))
        self.medio_d.place(x=760, y=160)
        self.anular_d = tk.Button(self, width=3,
                                  command=lambda: self.openNewWindow(self.anular_d, self.current_user.anular_d))
        self.anular_d.place(x=710, y=184)
        self.menhique_d = tk.Button(self, width=3,
                                    command=lambda: self.openNewWindow(self.menhique_d, self.current_user.menhique_d))
        self.menhique_d.place(x=660, y=230)
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
        # os.startfile("{}\main.exe".format(os.getcwd()))
        os.startfile("C:\IMAGEN\Enrollment.exe".format(os.getcwd()))

    def set_btn_valid(self, button, newWindow, field: Dedo):
        self.setIsLoading(True)
        print(filename)
        print("making the request...")

        category = Network.get_category(filename)
        category = str(category)[2:-1]
        field.category = category
        if (category != "arco"):
            # distance, encoded = Network.get_analisis_results(filename)
            # if distance is None or encoded is None:
            #     tk.messagebox.showerror("Registro Huella",
            #                             "No se encontro puntos caracteristicos en la huella, se la tomara de igual forma")
            field.huella_b64 = ""
            field.distance = 0
        self.setIsLoading(False)
        if category is not None:
            tk.messagebox.showinfo(
                "Registro Huella", "La huella de tipo {} ha sido registrada".format(category))
            button.configure(bg='green')
        else:
            tk.messagebox.showerror(
                "Registro Huella", "La huella no ha sido registrada")
            button.configure(bg='red')

        # w = tk.Message(self, text="this is a relatively long message", width=50).pack()

        newWindow.destroy()

    def resultsWindow(self):
        newWindow = tk.Toplevel(self)
        newWindow.title("Resultados")
        newWindow.geometry("400x400")
        font = ("Arial", "12", "bold italic")
        tk.Label(newWindow, text="RESUMEN DE CARACTERISTICAS",
                 font=font).place(x=100, y=50)
        tk.Label(newWindow, text="ARCOS:          {}".format(
            self.current_user.categ["arco"]), font=font).place(x=100, y=100)
        tk.Label(newWindow, text="PRESILLAS:      {}".format(
            self.current_user.categ["presilla"]), font=font).place(x=100, y=150)
        tk.Label(newWindow, text="VERTICILOS:     {}".format(
            self.current_user.categ["verticilo"]), font=font).place(x=100, y=200)
        tk.Label(newWindow, text="D10:            {}".format(
            self.current_user.d10), font=font).place(x=100, y=250)
        tk.Label(newWindow, text="SQTL:           {}".format(
            self.current_user.sqtl), font=font).place(x=100, y=300)
        tk.Label(newWindow, text="Análisis terminado", font=font).place(x=100, y=350)

        tk.Button(newWindow, text="Ok", command=lambda: self.controller.show_frame(
            "ResultFrame")).place(x=100, y=450)

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

        tk.Button(newWindow, text="TOMA DE HUELLAS", command=self.open_app).place(
            relx=0.5, rely=0.3, anchor=tk.CENTER)
        tk.Button(newWindow, text="Aceptar y Continuar",
                  command=lambda: self.set_btn_valid(btn, newWindow, field)).place(
            relx=0.5,
            rely=0.7,
            anchor=tk.CENTER)

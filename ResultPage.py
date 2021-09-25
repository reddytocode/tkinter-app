import tkinter as tk  # python 3
from tkinter import font as tkfont  # python 3
from PIL import Image, ImageTk
from network import Network
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL
from CurrentUserPersistance import get_user, Dedo, User


class ResultFrame(tk.Frame):

    def refresh(self):
        self.set_init()
        self.current_user = None
        self.setUserTable()
        font = ("Arial", "12", "bold italic")
        style_ORANGE = {"bg": '#EB5E00', "font": font}
        self.users = Network.get_all()
        print("self.users udated", self.users)
        names = ["{} - {}".format(index, user.name)
                 for index, user in enumerate(self.users)]

        # tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        tkvar = tk.StringVar(self)
        choices = names
        tkvar.set('')
        if choices:
            popupMenu = tk.OptionMenu(self, tkvar, *choices)
            popupMenu.place(x=10, y=45)
            tk.Label(self, text="Elija el usuario a mostrar",
                     bg='#ebac00', font=font).place(x=10, y=10)
        else:
            tk.Label(self, text="Aún no hay usuarios para mostrar",
                     bg='#ebac00', font=font).place(x=10, y=10)
        tk.Label(self, text="RESUMEN CARACTERISTICAS",
                 **style_ORANGE).place(x=400, y=10)

        self.current_user = None

        def change_dropdown(*args):
            global genero_aux
            genero_aux = tkvar.get().split(' - ')
            index = genero_aux[0]
            self.current_user = self.users[int(index)]
            self.setUserTable()
            print("chooosen", index)

        tkvar.trace('w', change_dropdown)
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.set_init()
        
    def set_init(self):
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

        self.users = Network.get_all()
        names = ["{} - {}".format(index, user.name)
                 for index, user in enumerate(self.users)]

        # tk.Label(self, bg='#ebac00', width=1000, height=561).place(x=0, y=0)
        tkvar = tk.StringVar(self)
        choices = names
        tkvar.set('')
        if choices:
            popupMenu = tk.OptionMenu(self, tkvar, *choices)
            popupMenu.place(x=10, y=45)
            tk.Label(self, text="Elija el usuario a mostrar",
                     bg='#ebac00', font=font).place(x=10, y=10)
        else:
            tk.Label(self, text="Aún no hay usuarios para mostrar",
                     bg='#ebac00', font=font).place(x=10, y=10)
        tk.Label(self, text="RESUMEN CARACTERISTICAS",
                 **style_ORANGE).place(x=400, y=10)

        self.current_user = None

        def change_dropdown(*args):
            global genero_aux
            genero_aux = tkvar.get().split(' - ')
            index = genero_aux[0]
            self.current_user = self.users[int(index)]
            self.setUserTable()
            print("chooosen", index)

        tkvar.trace('w', change_dropdown)


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

        if (self.current_user is not None):
            style = {"bg": '#ebac00', "font": font}
            style_ORANGE = {"bg": '#EB5E00', "font": font}
             
            tk.Label(self, width=43,
                     text="Nombres y Apellidos:   {} {}".format(
                         self.current_user.name, self.current_user.lastName),
                     **style).place(x=100, y=150)
            tk.Label(self, width=43,
                     text="CI:   {}".format(
                          self.current_user.ci), **style).place(x=100, y=175)
            tk.Label(self, width=43,
                     text="Fecha Nacimiento:   {}".format(
                          self.current_user.fechaNac), **style).place(x=100, y=200)
            tk.Label(self, width=43,
                     text="Telf:   {}".format(
                          self.current_user.telf), **style).place(x=100, y=225)
            
            
            
            tk.Label(self, text="ESTUDIO DE DERMATOGLIFOS",
                     **style).place(x=600, y=150)
            tk.Label(self, text="ARCOS:          {}  ".format(self.current_user.categ["arco"]), **style).place(x=600,
                                                                                                               y=200)
            tk.Label(self, text="PRESILLAS:      {}  ".format(self.current_user.categ["presilla"]), **style).place(x=600,
                                                                                                                   y=225)
            tk.Label(self, text="VERTICILOS:     {}  ".format(self.current_user.categ["verticilo"]), **style).place(x=600,
                                                                                                                    y=250)
            tk.Label(self, text="D10:            {}  ".format(
                self.current_user.d10), **style).place(x=750, y=200)
            tk.Label(self, text="SQTL:           {}  ".format(
                self.current_user.sqtl), **style).place(x=750, y=225)

            tk.Label(self, text="PREDOMINIO DE LAS CAPACIDADES DEPORTIVAS",
                     width=43, **style_ORANGE).place(x=100, y=275)
            tk.Label(self, text="{} - \"{}\"  ".format(self.current_user.res_primer_analisis,
                                                       self.current_user.formula_digital), width=43, **style).place(x=100, y=300)
            

            tk.Label(self, text="SE RECOMIENDA QUE TIENE APTITUDES PARA:",
                     width=43, **style_ORANGE).place(x=100, y=400)
            arco = self.current_user.categ["arco"]
            presilla = self.current_user.categ["presilla"]
            verticilo = self.current_user.categ["verticilo"]

            data = [arco, presilla, verticilo]
            may = max(data)
                
            max_data = data.index(may)
            name = ["Arco", "Presilla", "Verticilo"]
            msg_pred = ["Fuerza", "Velocidad",
                        "Coordinación motora"]
            
            predominancia = name[max_data]
            msg_pred = msg_pred[max_data]
            if data.count(may) > 1:
                predominancia = ""
                msg_pred = []
                for index, _ in enumerate(data):
                    if data[index] == may:
                        msg_pred.append(msg_pred[index])
                        msg_pred = " y ".join(msg_pred)
            
            tk.Label(self, text="PREDOMINANCIAS QUE DEBERIA EXPLOTAR",
                     width=43, **style_ORANGE).place(x=100, y=325)
            tk.Label(self, text=msg_pred, width=43, **style).place(x=100, y=350)
            
            X = [600, 625, 650]

            c_width = 225  # Define it's width
            c_height = 200  # Define it's height
            c = tk.Canvas(self, width=c_width, height=c_height, bg=style["bg"])
            c.place(x=600, y=300)

            # The variables below size the bar graph
            y_stretch = 15  # The highest y = max_data_value * y_stretch
            y_gap = 20  # The gap between lower canvas edge and x axis
            x_stretch = 10  # Stretch x wide enough to fit the variables
            x_width = 50  # The width of the x-axis
            x_gap = 20  # The gap between left canvas edge and y axis

            # A quick for loop to calculate the rectangle
            for x, y in enumerate(data):
                # coordinates of each bar
                # Bottom left coordinate
                x0 = x * x_stretch + x * x_width + x_gap

                # Top left coordinates
                y0 = c_height - (y * y_stretch + y_gap)

                # Bottom right coordinates
                x1 = x * x_stretch + x * x_width + x_width + x_gap

                # Top right coordinates
                y1 = c_height - y_gap

                # Draw the bar
                c.create_rectangle(x0, y0, x1, y1, fill="red")

                # Put the y value above the bar
                c.create_text(x0, y0, anchor=tk.SW,
                              text="{} - {}".format(name[x], str(y)))

            try:
                tk.Label(self, text="Recomendacion 1:{}".format(self.current_user.recomendacion1["deporte"]), width=43,
                         **style).place(x=100, y=425)
            except Exception as e:
                tk.Label(self, text="Recomendacion 1: No hay recomendacion",
                         width=43, **style).place(x=100, y=425)

            try:
                tk.Label(self, text="Recomendacion 2:{}".format(self.current_user.recomendacion2["deporte"]), width=43,
                         **style).place(x=100, y=450)
            except Exception as e:
                tk.Label(self, text="Recomendacion 2: No hay recomendacion",
                         width=43, **style).place(x=100, y=450)
            
            # add refresh button to refresh the page
            tk.Button(self, text="Refrescar", command=lambda: self.refresh()).place(x=600, y=100)
            

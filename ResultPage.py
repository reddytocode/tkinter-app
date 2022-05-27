from cgitb import small
import tkinter as tk
from PIL import Image, ImageTk

from CurrentUserPersistance import User
from network import Network

lw_msg = """
    Estos deportitas se centran naturalmente en
    generar la mayor poyencia con el menor peso
    corporal, manteniedo una alimentacion ideal
    podran practicar Boxeo, lucha, carreras de caballo,
    gimnasia y el salto de trampolin.
    """

wl_msg = """
    Los deportistas con resistencia y
    coordinación motora pasan largas horas
    en entrenamientos y competiciones los deportes
    ideales para ellos son las carreras de
    distancia, triatletas, nadadores de fondo y
    ciclistas.
    """
arco_msg = """
    Los deportistas que tiene huellas arco
    requieren un esfuerzo máximo y en los deportes
    que pueden practicar son: salto de altura,
    carrera 100m, levantamiento de pesas,
    lanzamientos, ciclismo en pista, baloncesto,
    voleibol y futbol.
    """
presilla_msg = """
    La velocidad representa la capacidad
    de realizar acciones corporales
    en un mínimo tiempo y con eficiencia. 
    Los reportes que puede practicar son:
    futbol, baloncesto, artes marciales, 
    tenis, gimnasia, boxeo, futbol americano y
    la mayoría de pruebas de atletismo.
    """
verticilo_msg = """
    La coordinación en la combinación
    física y motora que permite que el
    individuo pueda moverse o realizar algo,
    los deportes que puede practicar son:
    futbol, baloncesto, voleibol, natación,
    tenis y sus variantes, lanzamiento de
    bala, béisbol, lanza dardos y billar.
    """


class ResultFrame(tk.Frame):

    def refresh(self):
        self.set_init()
        self.current_user = None
        self.setUserTable()
        font = ("Arial", "12", "bold")
        style_ORANGE = {"bg": '#EB5E00', "font": font}
        self.users = Network.get_all()

        names = ["{} - {}".format(index, user.name).upper()
                 for index, user in enumerate(self.users)]

        tkvar = tk.StringVar(self)
        choices = names
        tkvar.set('')
        if choices:
            popupMenu = tk.OptionMenu(self, tkvar, *choices)
            popupMenu.place(x=10, y=45)
            tk.Label(self, text="Elija el usuario a mostrar".upper(),
                     bg='#ebac00', font=font).place(x=10, y=10)
        else:
            tk.Label(self, text="Aún no hay usuarios para mostrar".upper(),
                     bg='#ebac00', font=font).place(x=10, y=10)
        tk.Label(self, text="RESUMEN CARACTERÍSTICAS",
                 **style_ORANGE).place(x=400, y=10)

        self.current_user = None

        def change_dropdown(*args):
            global genero_aux
            genero_aux = tkvar.get().split(' - ')
            index = genero_aux[0]
            self.current_user = self.users[int(index)]
            self.setUserTable()

        tkvar.trace('w', change_dropdown)
    
    def remove(self):
        print("removing")
        Network.remove_user(self.current_user)
        self.refresh()
        
    def tkraise(self, aboveThis=None):
        self.refresh()
        return super(ResultFrame, self).tkraise()
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # original size 997 x 560
        self.base_width = 1100
        self.controller.geometry("1100x640")
        self.set_init()
        
    def set_init(self):
        font = ("Arial", "12", "bold")
        imageEmi = Image.open("image/fondopista.jpg")
        basewidth = self.base_width + 100
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

        tkvar.trace('w', change_dropdown)

        tk.Button(
            self,
            highlightbackground='#FFC638',
            text='VOLVER',
            font=('Arial Rounded MT Bold', 14),
            width=20,
            command=lambda: self.controller.show_frame("MainWindow")
        ).place(x=850, y=580)

    def setUserTable(self):
        font = ("Arial", "12", "bold")

        if (self.current_user is not None):
            style = {"bg": '#ebac00', "font": font}
            style_ORANGE = {"bg": '#EB5E00', "font": font}
            
            full_name = f"{self.current_user.name} {self.current_user.lastName}".upper()
            tk.Label(self, width=43,
                     text="NOMBRES:   {}".format(
                        full_name),
                     **style).place(x=100, y=150)
            final_ci = self.current_user.ci if self.current_user.ci else "--------------"
            tk.Label(self, width=43,
                     text="CI:   {}".format(
                          final_ci), **style).place(x=100, y=175)
            tk.Label(self, width=43,
                     text="FECHA DE NACIMIENTO:   {}".format(
                          self.current_user.fechaNac), **style).place(x=100, y=200)
            final_telf = self.current_user.telf if self.current_user.telf else "--------------"
            tk.Label(self, width=43,
                     text="TELF:   {}".format(
                          final_telf), **style).place(x=100, y=225)
            
            
            
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
            
            final_predominio = "{} - \"{}\"  ".format(self.current_user.res_primer_analisis, self.current_user.formula_digital)
            final_predominio = final_predominio.upper()
            tk.Label(
                self, 
                text=final_predominio, 
                width=43, 
                **style, 
            ).place(x=100, y=300)

            tk.Label(self, text="SE RECOMIENDA QUE TIENE APTITUDES PARA:",
                     width=43, **style_ORANGE).place(x=100, y=400)
            
            arco = self.current_user.categ["arco"]
            presilla = self.current_user.categ["presilla"]
            verticilo = self.current_user.categ["verticilo"]

            data = [arco, presilla, verticilo]
            may = max(data)
                
            max_data = data.index(may)
            name = ["Arco", "Presilla", "Verticilo"]
            msg_pred_arr = ["Fuerza", "Velocidad",
                        "Coordinación motora"]

            large_msgs_predominancia = [arco_msg, presilla_msg, verticilo_msg]

            large_msg_pred = large_msgs_predominancia[max_data]
            if self.current_user.formula_digital == "wl":
                large_msg_pred = wl_msg
            elif self.current_user.formula_digital == "lw":
                large_msg_pred = lw_msg

            msg_pred = msg_pred_arr[max_data]
            if data.count(may) > 1:
                arr = []
                for index, _ in enumerate(data):
                    if data[index] == may:
                        arr.append(msg_pred_arr[index])
                        msg_pred = " y ".join(arr)
            
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
            total = data[0] + data[1] + data[2]
            
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
                porcentaje = str(int(y * 100 / total)) + "%"
                c.create_text(x0 + x_width / 2, y0-10, text=porcentaje, font=font)
                # Put the y value above the bar
                c.create_text(x0, y0-20, anchor=tk.SW,
                              text="{} - {}".format(name[x], str(y)))

            recomendacion1, recomendacion2 = User.search_in_table(self.current_user.d10, self.current_user.tabla)
            try:
                deporte = recomendacion1["deporte"].title()
                # string capital letters
                tk.Label(self, text="Recomendacion 1:{}".format(deporte), width=43,
                         **style).place(x=100, y=425)
            except Exception as e:
                tk.Label(self, text="Recomendacion 1: No hay recomendacion",
                         width=43, **style).place(x=100, y=425)

            try:
                tk.Label(self, text="Recomendacion 2: {}".format(recomendacion2["deporte"]), width=43,
                         **style).place(x=100, y=450)
            except Exception as e:
                tk.Label(self, text="Recomendacion 2: No hay recomendacion",
                         width=43, **style).place(x=100, y=450)

            small_font = ("Arial", "11", "bold")
            small_style = {"bg": '#ebac00', "font": small_font} 

            tk.Label(
                self,
                text=large_msg_pred,
                width=43,
                height=7,
                **small_style
            ).place(x=100, y=500) 
            
            # add refresh button to refresh the page
            tk.Button(self, text="REFRESCAR", command=lambda: self.refresh()).place(x=600, y=100)

            tk.Button(self, bg='red', text="BORRAR",
                      command=lambda: self.remove()).place(x=800, y=100)
            

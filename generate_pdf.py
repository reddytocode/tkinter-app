from fpdf import FPDF
from CurrentUserPersistance import User
from network import Network
import os
import sys

lw_msg = ["Estos deportitas se centran naturalmente en generar la mayor poyencia con el menor peso",
          "corporal, manteniedo una alimentacion ideal podran practicar Boxeo, lucha, carreras de",
          "caballo, gimnasia y el salto de trampolin."
          ]

wl_msg = ["Los deportistas con resistencia y coordinación motora pasan largas horas",
          "en entrenamientos y competiciones los deportes ideales para ellos son las carreras",
          "de distancia, triatletas, nadadores de fondo y ciclistas."]
arco_msg = ["LOS DEPORTISTAS QUE TIENE LA CUALIDAD DE FUERZA, TIENE LA CAPACIDAD DE GENERAR UNA",
            "CONTRACCIÓN MUSCULAR SUPERIOR, LOS DEPORTES QUE PUEDEN PRACTICAR SON: SALTO DE ALTURA,",
            "CARRERA 100M, LEVANTAMIENTO DE PESAS, LANZAMIENTOS, CICLISMO EN PISTA, BALONCESTO,",
            "VOLEIBOL Y FUTBOL."]

presilla_msg = ["LOS DEPORTISTAS QUE TIENEN LA CUALIDAD DE VELOCIDAD TIENE LA CAPACIDAD",
                "DE REALIZAR ACCIONES CORPORALES EN UN MÍNIMO TIEMPO Y CON EFICIENCIA, LOS DEPORTES QUE",
                "PUEDEN PRACTICAR SON: FUTBOL, BALONCESTO, ARTES MARCIALES, TENIS, GIMNASIA, BOXEO Y LA ",
                "MAYORÍA DE PRUEBAS DE ATLETISMO."

                ]

verticilo_msg = ["LOS DEPORTISTAS QUE TIENEN LA CUALIDAD DE COORDINACIÓN, TIENE UNA COMBINACIÓN FÍSICA",
                 "Y MOTORA QUE PERMITE AL INDIVIDUO REALIZAR ALGO O MOVERSE DE UNA MANERA COORDINADA,",
                 "LOS DEPORTES QUE PUEDEN PRACTICAR SON: FUTBOL, BALONCESTO, VOLEIBOL, NATACIÓN,",
                 "TENIS Y SUS VARIANTES, LANZAMIENTO DE BALA, BÉISBOL, LANZA DARDOS Y BILLAR.",
                 ]


def set_bold(pdf):
    pdf.set_font("Arial", size=10, style="B")
    return pdf


def set_title_bold(pdf):
    pdf.set_font("Arial", size=15, style="B")
    return pdf


def set_font(pdf):
    pdf.set_font("Arial", size=10)
    return pdf


def create_table(pdf, table, padding=2):
    pdf = set_font(pdf)
    epw = pdf.w/2 - 2*pdf.l_margin
    pdf.cell(epw, 0.0, txt="", ln=2, align="C")
    col_width = epw/len(table[1][0])
    pdf = set_bold(pdf)
    pdf.cell(epw, 0.0, table[0][0], align='C')
    pdf = set_font(pdf)
    pdf.ln(0.5*25.4)
    th = pdf.font_size
    for row in table[1]:
        for datum in row:
            pdf.cell(col_width, padding*th, str(datum), border=1)
        pdf.ln(padding*th)
    return pdf


def generate_data(user_data):
    arco = user_data.categ["arco"]
    presilla = user_data.categ["presilla"]
    verticilo = user_data.categ["verticilo"]

    return [
        ['Estudio de dermatoglifos'],
        # headers
        [['Tipo', 'Cantidad'],
         # values
         ['Arco', arco],
         ['Presilla', presilla],
         ['Verticilo', verticilo],
         ['D10', user_data.d10],
         ['SQTL', user_data.sqtl],
         ]]


def get_predominancia(user):
    arco = user.categ["arco"]
    presilla = user.categ["presilla"]
    verticilo = user.categ["verticilo"]

    data = [arco, presilla, verticilo]
    may = max(data)
    max_data = data.index(may)
    msg_pred_arr = ["Fuerza", "Velocidad", "Coordinación motora"]

    large_msgs_predominancia = [arco_msg, presilla_msg, verticilo_msg]

    large_msg_pred = large_msgs_predominancia[max_data]
    if user.formula_digital == "wl":
        large_msg_pred = wl_msg
    elif user.formula_digital == "lw":
        large_msg_pred = lw_msg

    msg_pred = msg_pred_arr[max_data]
    if data.count(may) > 1:
        arr = []
        for index, _ in enumerate(data):
            if data[index] == may:
                arr.append(msg_pred_arr[index])
                msg_pred = " y ".join(arr)

    return msg_pred, large_msg_pred


def get_recomendaciones(user):
    recomendacion1, recomendacion2 = User.search_in_table(user.d10, user.tabla)
    try:
        deporte = recomendacion1["deporte"].title()
        recomendacion_1 = deporte
    except Exception:
        recomendacion_1 = "No hay recomendación"

    try:
        recomendacion_2 = recomendacion2["deporte"]
    except Exception:
        recomendacion_2 = "No hay recomendación"

    return recomendacion_1, recomendacion_2


def generate_pdf(user):
    pdf = FPDF()
    pdf.add_page()

    pdf = set_title_bold(pdf)
    pdf.cell(200, 10, txt="Reporte", ln=2, align="C")
    pdf = set_font(pdf)

    line = f"{user.name.capitalize()} {user.lastName.capitalize()}"
    pdf = set_bold(pdf)
    pdf.cell(200, 10, txt=line, ln=2)
    pdf = set_font(pdf)
    pdf.cell(200, 10, txt=f"CI: {user.ci}", ln=2)
    pdf.cell(200, 10, txt=f"Fecha de Nacimiento: {user.fechaNac}", ln=2)
    pdf.cell(200, 10, txt=f"Teléfono: {user.telf}", ln=2)
    pdf.cell(200, 10, txt="", ln=2)
    table = generate_data(user)
    pdf = create_table(pdf, table)

    pdf = set_font(pdf)
    pdf.cell(200, 10, txt="", ln=2)

    pdf = set_bold(pdf)
    pdf.cell(200, 10, txt="Predominio de las capacidades deportivas", ln=2)
    pdf = set_font(pdf)
    pdf.cell(
        200,
        10,
        txt=f"{user.res_primer_analisis} - {user.formula_digital}",
        ln=2
    )

    msg_1, msg_2 = get_predominancia(user)
    pdf = set_bold(pdf)
    pdf.cell(200, 10, txt="Predominancias que deberia explotar", ln=2)
    pdf = set_font(pdf)
    pdf.cell(200, 10, txt=msg_1, ln=2)
    pdf = set_bold(pdf)
    pdf.cell(200, 10, txt="Recomendación:", ln=2)
    pdf = set_font(pdf)
    for index, line in enumerate(msg_2):
        line = line.lower()
        if index == 0:
            line = line.capitalize()
        pdf.cell(200, 7, txt=line, ln=2)

    recomendacion_1, recomendacion_2 = get_recomendaciones(user)

    pdf = set_bold(pdf)
    pdf.cell(200, 10, txt="Se recomienda que tiene aptitudes para:", ln=2)
    pdf = set_font(pdf)
    pdf.cell(200, 10, txt=f"1. {recomendacion_1}", ln=2)
    pdf.cell(200, 10, txt=f"2. {recomendacion_2}", ln=2)

    pdf.output("reporte.pdf")

    # windows
    is_windows = hasattr(sys, 'getwindowsversion')
    if is_windows:
        path = f"{os.getcwd()}/reporte.pdf"
        os.startfile(path)
    else:
        os.system("open reporte.pdf")

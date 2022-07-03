import sys
import os
from fpdf import FPDF


def create_table(table, padding=2):
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font('Times', '', 10.0)
    epw = pdf.w/2 - 2*pdf.l_margin

    col_width = epw/len(table[1][0])
    pdf.set_font('Times', 'B', 14.0)
    pdf.cell(epw, 0.0, table[0][0], align='C')
    pdf.set_font('Times', '', 10.0)
    pdf.ln(0.5)
    th = pdf.font_size
    for row in table[1]:
        for datum in row:
            pdf.cell(col_width, padding*th, str(datum), border=1)
        pdf.ln(padding*th)
    pdf.ln(4*th)

    pdf.output('table-using-cell-borders.pdf', 'F')


def generate_data(arco, presilla, verticilo):
    return [
        ['Estudio de dermatoglifos'],
        # headers
        [['Tipo', 'Cantidad'],
         # values
         ['Arco', arco],
         ['Presilla', presilla],
         ['Verticilo', verticilo],
         ]]


table_1 = generate_data(arco=0, presilla=6, verticilo=4)
create_table(table_1)


is_windows = hasattr(sys, 'getwindowsversion')
if is_windows:
    path = f"{os.getcwd()}/reporte.pdf"
    os.startfile(path)
else:
    os.system("open table-using-cell-borders.pdf")

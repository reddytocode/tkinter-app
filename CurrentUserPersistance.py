current_user = None

def item_tabla(deporte, N, A, L, W, D10, SQTL):
    return {
        "deporte": deporte,
        "N": N,
        "A": A,
        "L": L,
        "W": W,
        "D10": D10,
        "SQTL": SQTL
    }

tabla = [
    item_tabla("Voleibol (2000)", 22, 1.00, 65.00, 34.00, 13.4, 125.6),
    item_tabla("Voleibol (1997)", 28, 0.70, 53.20, 46.10, 14.5, 133.8),
    item_tabla("Voleibol Femenino", 12, 12.00, 59.00, 29.00, 11.8, 98.6),
    item_tabla("Basquetbol", 35, 2.00, 60.00, 38.00, 12.6, 126.7),
    item_tabla("Basquetbol Masculino", 12, 5.00, 69.20, 25.80, 12.1, 12.1),
    item_tabla("Karate (1997)", 7, 0.00, 45.70, 54.30, 15.4, 159.7),
    item_tabla("Boxeo (1997)", 5, 0.00, 46.00, 54.00, 15.4, 143.4)
]

def search_in_table(d10, sqtl, tabla):
    def get_distance(item):
        return abs(sqtl-item['SQTL']) + abs(d10-item['D10'])
    opcion1 = None
    opcion2 = None
    param_1 = 10
    for item in tabla:
        distance = get_distance(item)
        if(distance < param_1):
            opcion2 = opcion1
            opcion1 = item

    print(opcion1)
    print(opcion2)

search_in_table(17, 139, tabla)

class Dedo:
    def to_json(self):
        return {
            "category": self.category,
            "distance": self.distance,
            "huella_b64": self.huella_b64
        }

    def __init__(self):
        self.category = None
        self.distance = 0
        self.huella_b64 = ""

    def is_valid(self):
        valid = self.category is not None
        print("valid", self.category, "id", valid)
        return valid


class User:
    def to_json(self):
        return {
            "name": self.name,
            "lastName": self.lastName,
            "ci": self.ci,
            "fechaNac": self.fechaNac,
            "telf": self.telf,
            "genero": self.genero,
            # dedos
            "pulgar_i": self.pulgar_i.to_json(),
            "anular_i": self.anular_i.to_json(),
            "medio_i": self.medio_i.to_json(),
            "indice_i": self.indice_i.to_json(),
            "menhique_i": self.menhique_i.to_json(),

            "pulgar_d": self.pulgar_d.to_json(),
            "anular_d": self.anular_d.to_json(),
            "medio_d": self.medio_d.to_json(),
            "indice_d": self.indice_d.to_json(),
            "menhique_d": self.menhique_d.to_json(),
            # res
            "res_primer_analisis": self.res_primer_analisis,
            "formula_digital": self.formula_digital,
            "categ": self.categ,  # = {"arco": 0, "presilla": 0, "verticilo": 0}
            "d10": self.d10,
            "sqtl": self.sqtl,
        }

    def __init__(self):
        # self.age = None
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

        self.pulgar_d = Dedo()
        self.anular_d = Dedo()
        self.medio_d = Dedo()
        self.indice_d = Dedo()
        self.menhique_d = Dedo()
        # res
        self.res_primer_analisis = None
        self.formula_digital = None
        self.categ = {"arco": 0, "presilla": 0, "verticilo": 0}
        self.d10 = 0
        self.sqtl = 0

    def print(self):
        print(self.name, "pulgar es:", self.pulgar_i.category)

    def primer_analisis(self):
        dedos = [self.pulgar_i, self.anular_i, self.medio_i, self.indice_i, self.menhique_i, self.pulgar_d,
                 self.anular_d, self.medio_d, self.indice_d, self.menhique_d]
        """
        arco => 1        (A)
        presilla => 2o 3 (L)
        verticillo => 4  (W)
        """
        for dedo in dedos:
            self.categ[dedo.category] += 1
        A = self.categ["arco"]
        L = self.categ["presilla"]
        W = self.categ["verticilo"]

        if (A == 10):
            self.res_primer_analisis = "FUERZA MAXIMA(no incluye potencia)"
            self.formula_digital = "10A"
        if (L >= 6 and W > 0 and A == 0):
            self.res_primer_analisis = "Velocidad, Potencia con un componente de resistencia y coordinacion"
            self.formula_digital = "LW"
        elif (W >= 5 and L > 0 and A == 0):
            self.res_primer_analisis = "Resistencia y Coordinacion de Velocidad y Potencia"
            self.formula_digital = "WL"
        elif (A > 0 and L > 0 and W == 0):
            self.res_primer_analisis = "FUERZA MAXIMA, VELOCIDAD Y POTENCIA"
            self.formula_digital = "AL"
        elif (A > 0 and L > 0 and W > 0):
            # OJO PREGUNTAR
            self.res_primer_analisis = "Depende de la mayor proporcion"
            self.formula_digital = "ALW"
        elif (L == 10):
            self.res_primer_analisis = "POTENCIA Y VELOCIDAD"
            self.formula_digital = "10L"
        elif (W == 10):
            self.res_primer_analisis = "RESISTENCIA Y COORDINACION"
            self.formula_digital = "10W"
        print("primer analisis: ", self.res_primer_analisis)

    def calculate_d10(self):
        A = self.categ["arco"]
        L = self.categ["presilla"]
        W = self.categ["verticilo"]
        self.d10 = L + 2*W

    def calculate_sqtl(self):
        dedos = [self.pulgar_i, self.anular_i, self.medio_i, self.indice_i, self.menhique_i, self.pulgar_d,
                 self.anular_d, self.medio_d, self.indice_d, self.menhique_d]
        sqtl = 0
        for dedo in dedos:
            sqtl+=dedo.distance
        self.sqtl = sqtl


def set_user(user):
    global current_user
    current_user = user


def get_user() -> User:
    global current_user
    return current_user

from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon
from helpers.menu import Menu
from classes.periodo_nota3 import Periodo_Nota3

class Periodo_Nota3_controller():
    def __init__(self):
        self.periodo_nota3 = Periodo_Nota3()
        self.salir = False

    def editar_periodo_nota3(self, id_periodo_nota3, curso):
        nota = input_data("Ingrese la nota del alumno >> ", "int")
        self.periodo_nota3.modificar_periodo_nota3({
            'id_periodo_nota3': id_periodo_nota3
        }, {
            curso: nota
        })
        print('''
        ========================
            Nota actualizada!!
        ========================
        ''')


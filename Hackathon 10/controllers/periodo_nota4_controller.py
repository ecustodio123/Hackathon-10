from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon
from helpers.menu import Menu
from classes.periodo_nota4 import Periodo_Nota4

class Periodo_Nota4_controller():
    def __init__(self):
        self.periodo_nota4 = Periodo_Nota4()
        self.salir = False

    def editar_periodo_nota4(self, id_periodo_nota4, curso):
        nota = input_data("Ingrese la nota del alumno >> ", "int")
        self.periodo_nota4.modificar_periodo_nota4({
            'id_periodo_nota4': id_periodo_nota4
        }, {
            curso: nota
        })
        print('''
        ========================
            Nota actualizada!!
        ========================
        ''')
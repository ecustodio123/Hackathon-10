from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon
from helpers.menu import Menu
from classes.periodo_nota2 import Periodo_Nota2

class Periodo_Nota2_controller():
    def __init__(self):
        self.periodo_nota2 = Periodo_Nota2()
        self.salir = False

    def editar_periodo_nota2(self, id_periodo_nota2, curso):
        nota = input_data("Ingrese la nota del alumno >> ", "int")
        self.periodo_nota2.modificar_periodo_nota2({
            'id_periodo_nota2': id_periodo_nota2
        }, {
            curso: nota
        })
        print('''
        ========================
            Nota actualizada!!
        ========================
        ''')


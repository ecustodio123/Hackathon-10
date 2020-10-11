from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon
from helpers.menu import Menu
from classes.periodo_nota1 import Periodo_Nota1

class Periodo_Nota1_controller():
    def __init__(self):
        self.periodo_nota1 = Periodo_Nota1()
        self.salir = False

    def editar_periodo_nota1(self, id_periodo_nota1, curso):
        nota = input_data("Ingrese la nota del alumno >> ", "int")
        self.periodo_nota1.modificar_periodo_nota1({
            'id_periodo_nota1': id_periodo_nota1
        }, {
            curso: nota
        })

        notas = self.periodo_nota1.obtener_periodo_nota1({'id_periodo_nota1': id_periodo_nota1})
        promedio = 0
        contador = 0
        for i in range(1, 6):
            if (notas[i] > 0 and notas[i] <= 20):
                contador += 1
                promedio += notas[i]
        promedio = promedio / contador
        self.periodo_nota1.modificar_periodo_nota1({
            'id_periodo_nota1': id_periodo_nota1
        }, {
            'promedio': promedio
        })


        print('''
        ========================
            Nota actualizada!!
        ========================
        ''')


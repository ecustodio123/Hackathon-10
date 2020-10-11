from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon, ingresar_dni, ingresar_curso, nombre_salon2
from helpers.menu import Menu
from classes.profesor import Profesor

class Profesor_controller():
    def __init__(self):
        self.profesor = Profesor()
        self.salir = False

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Profesor
                ===============
                ''')
                menu = ['Listar Profesores', 'Buscar Profesores', 'Nuevo Profesor', 'Salir']
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_profesores()
                elif respuesta == 2:
                    self.buscar_profesor()
                elif respuesta == 3:
                    self.insertar_profesor()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_profesores(self):
        print('''
        ==============================
            Lista de Profesores
        ==============================
        ''')
        profesores = self.profesor.obtener_profesores('id_profesor')
        print(print_table(profesores, ['ID', 'Nombre', 'DNI', 'Curso asignado', 'Salon 1', 'Salon 2', 'Salon 3']))
        input("\nPresione una tecla para continuar...")

    def buscar_profesor(self):
        print('''
        =======================
            Buscar Profesor
        =======================
        ''')
        try:
            id_profesor = input_data("Ingrese el ID del Profesor >> ", "int")
            profesor = self.profesor.obtener_profesor({'id_profesor': id_profesor})
            print(print_table(profesor, ['ID', 'Nombre', 'DNI', 'Curso asignado', 'Salon 1', 'Salon 2', 'Salon 3']))
            if profesor:
                if pregunta("¿Deseas dar mantenimiento al profesor selecionado?"):
                    opciones = ['Editar profesor', 'Eliminar profesor', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_profesor(id_profesor)
                    elif respuesta == 2:
                        self.eliminar_profesor(id_profesor)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_profesor(self):
        nombre = input_data("Ingrese el nombre del Profesor >> ")
        dni = ingresar_dni()
        condicion = True
        while condicion:
            num_salones = int(input("¿A cuantos salones enseña el profesor? (Recordar que el límite es de 3) >> "))
            if num_salones > 3 or num_salones < 0:
                print("Tiene que escoger una opción entre el 1 y el 3")
            else:
                condicion = False
        if num_salones == 1:
            salon1 = nombre_salon2()
            salon2 = ""
            salon3 = ""
        elif num_salones == 2:
            salon1 = nombre_salon2()
            salon2 = nombre_salon2()
            salon3 = ""
        elif num_salones == 3:
            salon1 = nombre_salon2()
            salon2 = nombre_salon2()
            salon3 = nombre_salon2()

        self.profesor.guardar_profesor({
            'nombre': nombre,
            'dni': dni,
            'curso': curso,
            'salon_1' : salon1,
            'salon_2' : salon2,
            'salon_3' : salon3
        })
        print('''
        ==============================
            Nuevo Alumno agregado !
        ==============================
        ''')

        self.listar_profesores()

    def editar_profesor(self, id_profesor):
        nombre = input_data("Ingrese el nuevo nombre del Profesor >> ")
        dni = input_data("Ingrese el nuevo DNI del Profesor >> ")
        curso = input_data("Ingrese el nuevo curso del Profesor >> ")
        
        self.profesor.modificar_profesor({
            'id_profesor': id_profesor
        }, {
            'nombre': nombre,
            'dni': dni,
            'curso': curso
        })
        print('''
        ========================
            Profesor Editado !
        ========================
        ''')

    def eliminar_profesor(self, id_profesor):
        self.profesor.eliminar_profesor({
            'id_profesor': id_profesor
        })

        print('''
        ============================
            Profesor Eliminado !
        ============================
        ''')

from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon
from helpers.menu import Menu
from classes.alumno import Alumno
from classes.notas_bimestre import Notas_bimestre
from classes.periodo_nota1 import Periodo_Nota1
from classes.periodo_nota2 import Periodo_Nota2
from classes.periodo_nota3 import Periodo_Nota3
from classes.periodo_nota4 import Periodo_Nota4
from connection.conn import Conexion

class Alumno_controller():
    def __init__(self):
        self.alumno = Alumno()
        self.salir = False
        self.periodo_nota1 = Periodo_Nota1()
        self.periodo_nota2 = Periodo_Nota2()
        self.periodo_nota3 = Periodo_Nota3()
        self.periodo_nota4 = Periodo_Nota4()
        self.notas_bimestre = Notas_bimestre()

    def menu(self):
        while True:
            try:
                print('''
                ===============
                    Alumno
                ===============
                ''')
                menu = ['Listar Alumnos', 'Buscar Alumno', 'Nuevo Alumno', 'Salir']
                respuesta = Menu(menu).show()

                if respuesta == 1:
                    self.listar_alumnos()
                elif respuesta == 2:
                    self.buscar_alumno()
                elif respuesta == 3:
                    self.insertar_alumno()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_alumnos(self):
        print('''
        ========================
            Lista de Alumnos
        ========================
        ''')
        alumnos = self.alumno.obtener_alumnos('id_alumno')
        print(print_table(alumnos, ['ID', 'Nombres', 'Códgo', 'Salón', 'id_periodo_1', 'id_periodo_2', 'id_periodo_3', 'id_periodo_4']))
        input("\nPresione una tecla para continuar...")

    def buscar_alumno(self):
        print('''
        =====================
            Buscar Alumno
        =====================
        ''')
        try:
            id_alumno = input_data("Ingrese el ID del Alumno >> ", "int")
            alumno = self.alumno.obtener_alumno({'id_alumno': id_alumno})
            print(print_table(alumno, ['ID', 'Nombres', 'Códgo', 'Salón', 'id_periodo_1', 'id_periodo_2', 'id_periodo_3', 'id_periodo_4']))
            if alumno:
                if pregunta("¿Deseas dar mantenimiento al alumno?"):
                    opciones = ['Editar alumno', 'Eliminar alumno', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_alumno(id_alumno)
                    elif respuesta == 2:
                        self.eliminar_alumno(id_alumno)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_alumno(self):
        nombre = input_data("Ingrese el nombre del alumno >> ")
        codigo = input_codigo()
        print("\nPor favor introduzca el salón al cual corresponda el alumno:")
        salones = ['1° Primaria', '2° Primaria', '3° Primaria', '4° Primaria', '5° Primaria', '6° Primaria', '1° Secundaria', '2° Secundaria', '3° Secundaria', '4° Secundaria', '5° Secundaria']
        salon = Menu(salones).show()
        salon = nombre_salon(salon)


        self.alumno.guardar_alumno({
            'nombre': nombre,
            'codigo': codigo,
            'salon': salon
        })
        print('''
        ==============================
            Nuevo Alumno agregado !
        ==============================
        ''')

        self.periodo_nota1.guardar_periodo_nota1({
            'matematica': None,
            'religion': 77,
            'comunicacion': 77,
            'ingles': 77,
            'historia': 77,
            'promedio': 77
        })

        self.periodo_nota2.guardar_periodo_nota2({
            'matematica': 77,
            'religion': 77,
            'comunicacion': 77,
            'ingles': 77,
            'historia': 77,
            'promedio': 77
        })

        self.periodo_nota3.guardar_periodo_nota3({
            'matematica': 77,
            'religion': 77,
            'comunicacion': 77,
            'ingles': 77,
            'historia': 77,
            'promedio': 77
        })

        self.periodo_nota4.guardar_periodo_nota4({
            'matematica': 77,
            'religion': 77,
            'comunicacion': 77,
            'ingles': 77,
            'historia': 77,
            'promedio': 77
        })

        self.listar_alumnos()

    def editar_alumno(self, id_alumno):
        nombre = input_data("Ingrese el nuevo nombre del alumno >> ")
        print("\nPor favor introduzca el nuevo salón al cual corresponda el alumno:")
        salones = ['1° Primaria', '2° Primaria', '3° Primaria', '4° Primaria', '5° Primaria', '6° Primaria', '1° Secundaria', '2° Secundaria', '3° Secundaria', '4° Secundaria', '5° Secundaria']
        salon = Menu(salones).show()
        salon = nombre_salon(salon)
        self.alumno.modificar_alumno({
            'id_alumno': id_alumno
        }, {
            'nombre': nombre,
            'salon': salon
        })
        print('''
        ========================
            Alumno Editado !
        ========================
        ''')

    def eliminar_alumno(self, id_alumno):
        self.alumno.eliminar_alumno({
            'id_alumno': id_alumno
        })
        self.periodo_nota1.eliminar_periodo_nota1({
            'id_periodo_nota1' : id_alumno
        })
        self.periodo_nota2.eliminar_periodo_nota2({
            'id_periodo_nota2' : id_alumno
        })
        self.periodo_nota3.eliminar_periodo_nota3({
            'id_periodo_nota3' : id_alumno
        })
        self.periodo_nota4.eliminar_periodo_nota4({
            'id_periodo_nota4' : id_alumno
        })


        print('''
        ========================
            Alumno Eliminado !
        ========================
        ''')

    def mostrar_alumno(self):
        id_alumno = input_data("Ingrese el ID del alumno que esta buscando>> ")
        alumno = self.alumno.obtener_alumno({'id_alumno': id_alumno})
        print(print_table(alumno, ['ID', 'Nombres', 'Códgo', 'Salón', 'id_periodo_1', 'id_periodo_2', 'id_periodo_3', 'id_periodo_4']))
        if alumno:
            menu = ["1° Bimestre", "2° Bimestre", "3° Bimestre", "4° Bimestre"]
            bimestre = Menu(menu).show()
            if bimestre == 1:
                periodo = 'periodo_nota1'
                bim = "Primer Bimestre"
            elif bimestre == 2:
                periodo = 'periodo_nota2'
                bim = "Segundo Bimestre"
            elif bimestre == 3:
                periodo = 'periodo_nota3'
                bim = "Tercer Bimestre"
            elif bimestre == 4:
                periodo = 'periodo_nota4'
                bim = "Cuarto Bimestre"
            
            try: 
                conn = Conexion(periodo)
                query = '''
                DROP TABLE IF EXISTS notas_bimestre;
                '''
                conn.ejecutar_sentencia(query)
            except Exception as e:
                print(f'{str(e)}')

            try:
                conn = Conexion(periodo)
                query = '''
                    CREATE TABLE IF NOT EXISTS notas_bimestre(
                        id_notas_bimestre SERIAL PRIMARY KEY NOT NULL,
                        nombre varchar(50) NOT NULL,
                        codigo varchar(50) NOT NULL,
                        salon varchar(50) NOT NULL,
                        matematica decimal,
                        religion decimal,
                        comunicacion decimal,
                        ingles decimal,
                        historia decimal,
                        promedio decimal
                    );
                '''
                conn.ejecutar_sentencia(query)

            except Exception as e:
                print(f'{str(e)}')

                
            try:
                conn = Conexion(periodo)
                query = f'''
                INSERT INTO notas_bimestre(nombre, codigo, salon, matematica, religion, comunicacion, ingles, historia, promedio)  SELECT nombre, codigo, salon, matematica, religion, comunicacion, ingles, historia, promedio FROM alumnos  INNER JOIN {periodo} on alumnos.id_{periodo} = {periodo}.id_{periodo} WHERE alumnos.id_alumno={id_alumno}
                '''
                cursor = conn.execute_query(query)
                conn.commit()

            except Exception as e:
                print(f'{str(e)}')

            finally:
                conn.close_connection()
            
            notas_bimestre = Notas_bimestre()
            print(f'''
                ======================================================
                    Notas del alumno {alumno[1]} en el {bim}
                =======================================================
                ''')
            notas = self.notas_bimestre.obtener_notas_bimestre('id_notas_bimestre')
            print(print_table(notas, ['ID', 'Nombre', 'Códgo', 'Salón', 'Matemática', 'Religión', 'Comunicación', 'Inglés', 'Historia', 'Promedio']))
            input("\nPresione una tecla para continuar...")

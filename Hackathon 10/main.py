from helpers.helper import input_data, print_table, pregunta, input_codigo, input_fecha, nombre_salon, ingresar_curso
from helpers.menu import Menu
from controllers.rol_controller import Roles_controller
from controllers.alumno_controller import Alumno_controller
from controllers.profesor_controller import Profesor_controller
from controllers.periodo_nota1_controller import Periodo_Nota1_controller
from controllers.periodo_nota2_controller import Periodo_Nota2_controller
from controllers.periodo_nota3_controller import Periodo_Nota3_controller
from controllers.periodo_nota4_controller import Periodo_Nota4_controller

def iniciar_app():
    try:
        print('''
        ===============================
            Colegio - El Grupo 03
        ===============================
        ''')
        print("Bienvenido, por favor indique su cargo\n")
        menu_inicio = ["Administrador", "Alumno", "Profesor", "Salir"]
        respuesta = Menu(menu_inicio).show()
        if respuesta == 1:
            rol = Roles_controller()
            rol.inicio_admin()
            if rol.admin:
                menu_principal = ["Registrar nuevo usuario", "Ver información de los alumnos", "Ver información de los profesores", "Ver las notas de los alumnos por salones y bimestres", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    rol = Roles_controller()
                    rol.menu()
                    if rol.salir:
                        iniciar_app()
                elif respuesta == 2:
                    alumno = Alumno_controller()
                    alumno.menu()
                    if alumno.salir:
                        iniciar_app()
                elif respuesta == 3:
                    profesor = Profesor_controller()
                    profesor.menu()
                    if profesor.salir:
                        iniciar_app()
                elif respuesta == 4:
                    alumno = Alumno_controller()
                    alumno.listar_alumnos()
                    try:
                        alumno.mostrar_alumno()
                    except Exception as e:
                        print(f'{str(e)}')
                    input("\nPresione una tecla para continuar...")
                    # cajero = Cajero_controller()
                    # cajero.reporte_mes()
                    # iniciar_app()

        elif respuesta == 2:
            rol = Roles_controller()
            rol.inicio_alumno()
            if rol.alumno:
                alumno = Alumno_controller()
                menu_principal = ["Ver el registro de alumnos completo", "Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    alumno.listar_alumnos()
                    print("\nUsted como alumno solo puede ver a los alummos, no puede hacer modificaciones")
            iniciar_app()
        
        elif respuesta == 3:
            rol = Roles_controller()
            rol.inicio_profesor()
            if rol.profesor:
                profesor = Profesor_controller()
                menu_principal = ["Ver el registro de profesores completo", "Insertar notas","Salir"]
                respuesta = Menu(menu_principal).show()
                if respuesta == 1:
                    profesor.listar_profesores()
                    print("\nUsted como profesor solo puede ver a los otros profesores regustradis, no puede hacer modificaciones")
                if respuesta == 2:
                    alumno = Alumno_controller()
                    print("\nEstos son todos la lista de alumnos: ")
                    alumno.listar_alumnos()
                    id_periodo_nota = int(input("Por favor introduzca el ID del alumno al cual va ingresar la nota>> "))
                    curso = ingresar_curso("¿A que curso usted está asignado?")
                    print("\nA continuación indique el bimestre en el cual va colocar la nota:")
                    menu = ["Primer Bimestre", "Segundo Bimestre", "Tercer Bimestre", "Cuarto Bimestre"]
                    periodo = Menu(menu).show()
                    if periodo == 1:
                        periodo_Nota1 = Periodo_Nota1_controller()
                        periodo_Nota1.editar_periodo_nota1(id_periodo_nota, curso)
                    elif periodo == 2:
                        periodo_Nota2 = Periodo_Nota2_controller()
                        periodo_Nota2.editar_periodo_nota2(id_periodo_nota, curso)
                    elif periodo == 3:
                        periodo_Nota3 = Periodo_Nota3_controller()
                        periodo_Nota3.editar_periodo_nota3(id_periodo_nota, curso)
                    elif periodo == 4:
                        periodo_Nota4 = Periodo_Nota4_controller()
                        periodo_Nota4.editar_periodo_nota4(id_periodo_nota, curso)
                        
                    
                if profesor.salir:
                    iniciar_app()

    print("\nGracias por utilizar el sistema\n")


    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()
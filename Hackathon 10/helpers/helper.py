from prettytable import PrettyTable
import random
from helpers.menu import Menu

def print_table(data, header=[]):
    tabla = 'Algo ocurrio mal'
    if not data:
        raise ValueError('No hay ningún dato para mostrar')

    if isinstance(data, list):
        if isinstance(data[0], dict):
            header = list(data[0].keys())
            tabla = PrettyTable(header)
            for row in data:
                tabla.add_row(list(row.values()))
        elif isinstance(data[0], tuple):
            header = table_header(data[0], header)
            tabla = PrettyTable(header)
            for row in data:
                tabla.add_row(list(row))
    elif isinstance(data, dict):
        header = list(data.keys())
        tabla = PrettyTable(header)
        tabla.add_row(list(data.values()))
    elif isinstance(data, tuple):
        header = table_header(data, header)
        tabla = PrettyTable(header)
        tabla.add_row(list(data))
    return tabla

def table_header(data, head):
    if not head:
        head = list(range(1, len(data) + 1))
    if len(head) < len(data):
        head.extend(list(range(len(head) + 1, len(data) + 1)))
    if len(head) > len(data):
        del head[len(data):]
    return head

def input_data(texto, tipo='string'):
    while True:
        try:
            if tipo == 'string':
                dato = input(texto).strip()
            elif tipo == 'int':
                dato = int(input(texto).strip())
            elif tipo == 'float':
                dato = float(input(texto).strip())

            if str(dato):
                if (isinstance(dato, int) or isinstance(dato, float)) and dato < 0:
                    raise ValueError("")
                break
            else:
                print("No ingreso ningún dato")
        except ValueError:
            print('Debes ingresar el tipo de dato correcto')
    return dato

def pregunta(texto):
    print(f'\n{texto}\n')
    response = False
    while True:
        dato = input("Seleccione (si) o (no) >> ").strip()
        if dato.lower() == 'si':
            response = True
            break
        elif dato.lower() == 'no':
            response = False
            break
        else:
            print('Debe elegir una opción...')
    print("\n")
    return response

def cargo(texto):
    print(f'\n{texto}\n')
    while True:
        dato = input("Seleccione (admin) o (alumno) o (profesor)>> ").strip()
        if dato.lower() == 'admin':
            response = dato.lower()
            break
        elif dato.lower() == 'alumno':
            response = dato.lower()
            break
        elif dato.lower() == 'profesor':
            response = dato.lower()
            break
        else:
            print('Debe elegir una opción...')
    print("\n")
    return response

def ingresar_curso(texto):
    print(f'\n{texto}\n')
    while True:
        dato = input("Seleccione (matematica) o (religion) o (comunicacion) o (ingles) o (historia)>> ").strip()
        if dato.lower() == 'matematica':
            response = dato.lower()
            break
        elif dato.lower() == 'religion':
            response = dato.lower()
            break
        elif dato.lower() == 'comunicacion':
            response = dato.lower()
            break
        elif dato.lower() == 'ingles':
            response = dato.lower()
            break
        elif dato.lower() == 'historia':
            response = dato.lower()
            break
        else:
            print('Debe elegir una opción...')
    print("\n")
    return response

def input_fecha():
    while True:
        try:
            while  True:
                dia = int(input("\nPor favor ingrese el día correspondiente a la fecha >> "))
                if  int(dia) > 0 and int(dia) <=31:
                    # print(dia)
                    break
                else:
                    print("\nDebes ingresar una día entre el 1 al 31")

            while True:
                mes = int(input("\nPor favor ingrese el mes correspondiente a la fecha >> "))
                if  int(mes) > 0 and int(mes) <=12:
                    # print(mes)
                    break
                else:
                    print("\nDebes ingresar un mes entre el 1 al 12")

            while True:
                anio = int(input("\nPor favor ingrese el año correspondiente a la fecha >> "))
                if  int(anio) >= 2000 and int(anio) <=2030:
                    # print(anio)
                    break
                else:
                    print("\nDebes ingresar un año entre el 2000 al 2030")
            fecha = str(anio)+"/"+str(mes)+"/"+str(dia)
            # print(fecha)
            break
        except ValueError:
            print('\nDebes ingresar el tipo de dato correcto')
    return fecha

def ingresar_dni():
    while True:
        try:
            dni = input("\nPor favor introduzca su DNI >>")
            if (len(dni) != 8):
                print("\nLos DNI tienen 8 digitos")
            else:
                break
        except ValueError:
            print('Debes ingresar el tipo de dato correcto')
    return dni

def input_codigo():
    codigo = []
    codigo.append(str(random.randint(2019 , 2021)))
    codigo.append("-")
    codigo.append(str(random.randint(1000 , 9999)))
    codigo.append("-")
    codigo.append(str(random.randint(1 , 99)))
    codigo.append("-")
    codigo.append(str(random.randint(1 , 10)))

    # print(codigo)
    codigo = "".join(codigo)
    # print(codigo)
    return codigo

def nombre_mes(mes):
    if mes == '1':
        return 'enero'
    elif mes == '2':
        return 'febrero'
    elif mes == '3':
        return 'marzo'
    elif mes == '4':
        return 'abril'
    elif mes == '5':
        return 'mayo'
    elif mes == '6':
        return 'junio'
    elif mes == '7':
        return 'julio'
    elif mes == '8':
        return 'agosto'
    elif mes == '9':
        return 'septiembre'
    elif mes == '10':
        return 'octubre'
    elif mes == '11':
        return 'noviembre'
    elif mes == '12':
        return 'diciembre'

def nombre_salon(salon):
    if salon == 1:
        return '1° Primaria'
    elif salon == 2:
        return '2° Primaria'
    elif salon == 3:
        return '3° Primaria'
    elif salon == 4:
        return '4° Primaria'
    elif salon == 5:
        return '5° Primaria'
    elif salon == 6:
        return '6° Primaria'
    elif salon == 7:
        return '1° Secundaria'
    elif salon == 8:
        return '2° Secundaria'
    elif salon == 9:
        return '3° Secundaria'
    elif salon == 10:
        return '4° Secundaria'
    elif salon == 11:
        return '5° Secundaria'

def nombre_salon2():
    salones = ['1° Primaria', '2° Primaria', '3° Primaria', '4° Primaria', '5° Primaria', '6° Primaria', '1° Secundaria', '2° Secundaria', '3° Secundaria', '4° Secundaria', '5° Secundaria']
    salon = Menu(salones).show()
    if salon == 1:
        return '1° Primaria'
    elif salon == 2:
        return '2° Primaria'
    elif salon == 3:
        return '3° Primaria'
    elif salon == 4:
        return '4° Primaria'
    elif salon == 5:
        return '5° Primaria'
    elif salon == 6:
        return '6° Primaria'
    elif salon == 7:
        return '1° Secundaria'
    elif salon == 8:
        return '2° Secundaria'
    elif salon == 9:
        return '3° Secundaria'
    elif salon == 10:
        return '4° Secundaria'
    elif salon == 11:
        return '5° Secundaria'

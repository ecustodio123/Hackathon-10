from connection.conn import Conexion

class Alumno:
    def __init__(self):
        self.model = Conexion('alumnos')

    def guardar_alumno(self, alumno):
        return self.model.insert(alumno)

    def obtener_alumno(self, id_alumno):
        return self.model.get_by_id(id_alumno)

    def obtener_alumnos(self, order):
        return self.model.get_all(order)

    def buscar_alumnos(self, data_alumno):
        return self.model.get_by_column(data_alumno)

    def modificar_alumno(self, id_alumno, data_alumno):
        return self.model.update(id_alumno, data_alumno)

    def eliminar_alumno(self, id_alumno):
        return self.model.delete(id_alumno)
    
    def buscar_alumno_like(self, data_alumno):
        return self.model.where_like(data_alumno)

    def inner_alumno(self, tabla_union):
        return self.model.inner_notas(tabla_union)

    # def buscar_usuario(self, data):
    #     return self.model.where_name(data)

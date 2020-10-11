from connection.conn import Conexion

class Notas_bimestre:
    def __init__(self):
        self.model = Conexion('notas_bimestre')

    def guardar_notas_bimestre(self, notas_bimestre):
        return self.model.insert(notas_bimestre)

    def obtener_nota_bimestre(self, id_notas_bimestre):
        return self.model.get_by_id(id_notas_bimestre)

    def obtener_notas_bimestre(self, order):
        return self.model.get_all(order)

    def buscar_notas_bimestre(self, data_notas_bimestre):
        return self.model.get_by_column(data_notas_bimestre)

    def modificar_notas_bimestre(self, id_notas_bimestre, data_notas_bimestre):
        return self.model.update(id_notas_bimestre, data_notas_bimestre)

    def eliminar_notas_bimestre(self, id_notas_bimestre):
        return self.model.delete(id_notas_bimestre)
    
    def buscar_notas_bimestre_like(self, data_notas_bimestre):
        return self.model.where_like(data_notas_bimestre)

    def inner_notas_bimestre(self, tabla_union):
        return self.model.inner_notas(tabla_union)

    # def buscar_usuario(self, data):
    #     return self.model.where_name(data)

from connection.conn import Conexion

class Periodo_Nota1:
    def __init__(self):
        self.model = Conexion('periodo_nota1')

    def guardar_periodo_nota1(self, periodo_nota1):
        return self.model.insert(periodo_nota1)

    def obtener_periodo_nota1(self, id_periodo_nota1):
        return self.model.get_by_id(id_periodo_nota1)

    def obtener_periodo_notas1(self, order):
        return self.model.get_all(order)

    def buscar_periodo_notas1(self, data_periodo_nota1):
        return self.model.get_by_column(data_periodo_nota1)

    def modificar_periodo_nota1(self, id_periodo_nota1, data_periodo_nota1):
        return self.model.update(id_periodo_nota1, data_periodo_nota1)

    def eliminar_periodo_nota1(self, id_periodo_nota1):
        return self.model.delete(id_periodo_nota1)
    
    def buscar_periodo_nota1_like(self, data_periodo_nota1):
        return self.model.where_like(data_periodo_nota1)

    # def buscar_usuario(self, data):
    #     return self.model.where_name(data)

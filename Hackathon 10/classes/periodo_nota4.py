from connection.conn import Conexion

class Periodo_Nota4:
    def __init__(self):
        self.model = Conexion('periodo_nota4')

    def guardar_periodo_nota4(self, periodo_nota4):
        return self.model.insert(periodo_nota4)

    def obtener_periodo_nota4(self, id_periodo_nota4):
        return self.model.get_by_id(id_periodo_nota4)

    def obtener_periodo_notas4(self, order):
        return self.model.get_all(order)

    def buscar_periodo_notas4(self, data_periodo_nota4):
        return self.model.get_by_column(data_periodo_nota4)

    def modificar_periodo_nota4(self, id_periodo_nota4, data_periodo_nota4):
        return self.model.update(id_periodo_nota4, data_periodo_nota4)

    def eliminar_periodo_nota4(self, id_periodo_nota4):
        return self.model.delete(id_periodo_nota4)
    
    def buscar_periodo_nota4_like(self, data_periodo_nota4):
        return self.model.where_like(data_periodo_nota4)

    # def buscar_usuario(self, data):
    #     return self.model.where_name(data)

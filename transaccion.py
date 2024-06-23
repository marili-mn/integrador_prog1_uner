class Transaccion:
    def __init__(self, item_id, id_vehiculo, id_cliente, tipo_transaccion, fecha, monto, observaciones):
        self.item_id = item_id
        self.id_vehiculo = id_vehiculo
        self.id_cliente = id_cliente
        self.tipo_transaccion = tipo_transaccion
        self.fecha = fecha
        self.monto = monto
        self.observaciones = observaciones 

    def a_dict(self):
        return {
            'item_id': self.item_id,
            'id_vehiculo': self.id_vehiculo,
            'id_cliente': self.id_cliente,
            'tipo_transaccion': self.tipo_transaccion,
            'fecha': self.fecha,
            'monto': self.monto,
            'observaciones': self.observaciones
        }

class Transaccion:
    def __init__(self, item_id, cliente_id, auto_id, precio_venta):
        self.item_id = item_id
        self.cliente_id = cliente_id
        self.auto_id = auto_id
        self.precio_venta = precio_venta

    def a_dict(self):
        return {
            'item_id': self.item_id,
            'cliente_id': self.cliente_id,
            'auto_id': self.auto_id,
            'precio_venta': self.precio_venta
        }

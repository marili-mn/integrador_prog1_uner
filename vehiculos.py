class Vehiculos:
    def __init__(self, item_id, patente, marca, modelo, tipo_vehiculo, anio, kilometraje, precio_compra, precio_venta, estado):
        self.item_id = item_id
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.tipo_vehiculo = tipo_vehiculo
        self.anio = anio
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.estado = estado

    def a_dict(self):
        return {
            'item_id': self.item_id,
            'patente': self.patente,
            'marca': self.marca,
            'modelo': self.modelo,
            'tipo_vehiculo': self.tipo_vehiculo,
            'anio': self.anio,
            'kilometraje': self.kilometraje,
            'precio_compra': self.precio_compra,
            'precio_venta': self.precio_venta,
            'estado': self.estado
        }

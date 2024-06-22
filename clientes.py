class Clientes:
    def __init__(self, item_id, nombre, documento, apellido, direccion, celular, email):
        self.item_id = item_id
        self.nombre = nombre
        self.documento = documento
        self.apellido = apellido
        self.direccion = direccion
        self.celular = celular
        self.email = email

    def a_dict(self):
        return {
            'item_id': self.item_id,
            'nombre': self.nombre,
            'documento': self.documento,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'celular': self.celular,
            'email': self.email
        }

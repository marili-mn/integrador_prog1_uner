import sys
from vehicle import Vehicle
from customer import Customer
from transaction import Transaction
from database import Database
#   Importamos las clases de los json

class InterfazConcesionario:
    def __init__(self):
        self.vehiculosDb = Database('data/vehiculos.json')
        self.customDb = Database('data/clientes.json')
        self.transaccionesDb = Database('data/transacciones.json')

    def mainMenu(self):
        while True:
            choice = input("""
    1. Gestionar Vehiculos
    2. Gestionar Clientes
    3. Registrar Transaccion
    4. Salir          
    Seleccione una opcion: """
                        )                       
            if choice == '1':
                self.modificarVehiculos()
            elif choice == '2':
                self.administrarCustomers()
            elif choice == '3':
                self.administrarTransacciones()
            elif choice == '4':
                sys.exit()
            else:
                print("Opcion invalida, por favor intentelo nuevamente.")

    def modificarVehiculos(self):
        while True:
            print("\n1. Crear Vehiculo")
            print("2. Editar Vehiculo")
            print("3. Eliminar Vehiculo")
            print("4. Listar Vehiculos")
            print("5. Volver al menu principal")
            choice = input("Seleccione una opcion: ")
            if choice == '1':
                self.crearVehiculo()
            elif choice == '2':
                self.editarVehiculo()
            elif choice == '3':
                self.eliminarVehiculo()
            elif choice == '4':
                self.listarVehiculos()
            elif choice == '5':
                return
            else:
                print("Opcion invalida, por favor intente nuevamente.")

    def crearVehiculo(self):
        # Solicitar datos y crear el vehiculo
        patente = input("Ingrese la patente del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        tipoVehiculo = input("Ingrese el tipo del vehiculo (Sedán, SUV, Pick Up, etc): ")
        anio = int(input("Ingrese el año del vehiculo: "))
        kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
        precioCompra = float(input("Ingrese el precio de compra del vehiculo: "))
        precioVenta = float(input("Ingrese el precio de venta del vehiculo: "))
        estado = input("Ingrese el estado del vehiculo (Disponible, Reservado, Vendido): ")

        vehiculoId = len(self.vehiculosDb.obtenerTodosLosRegistros()) + 1
        nuevoVehiculo = Vehicle(vehiculoId, patente, marca, modelo, tipoVehiculo, anio, kilometraje, precioCompra, precioVenta, estado)
        self.vehiculosDb.agregarRegistro(nuevoVehiculo.a_dict())
        print("Vehiculo creado correctamente.")

    def editarVehiculo(self):
        # Solicitar ID del vehículo y editar los datos
        vehiculoId = int(input("Ingrese el ID del vehiculo a editar: "))
        vehiculo = self.vehiculosDb.buscarRegistrosPorId(vehiculoId)
        if vehiculo:
            print("Deje en blanco si no desea modificar el campo.")
            patente = input(f"Patente actual ({vehiculo['patente']}): ") or vehiculo['patente']
            marca = input(f"Marca actual ({vehiculo['marca']}): ") or vehiculo['marca']
            modelo = input(f"Modelo actual ({vehiculo['modelo']}): ") or vehiculo['modelo']
            tipoVehiculo = input(f"Tipo actual ({vehiculo['tipo']}): ") or vehiculo['tipo']
            anio = input(f"Año actual ({vehiculo['anio']}): ") or vehiculo['anio']
            kilometraje = input(f"Kilometraje actual ({vehiculo['kilometraje']}): ") or vehiculo['kilometraje']
            precioCompra = input(f"Precio de compra actual ({vehiculo['precioCompra']}): ") or vehiculo['precioCompra']
            precioVenta = input(f"Precio de venta actual ({vehiculo['precioVenta']}): ") or vehiculo['precioVenta']
            estado = input(f"Estado actual ({vehiculo['estado']}): ") or vehiculo['estado']

            actualizarVehiculo = Vehicle(vehiculoId, patente, marca, modelo, tipoVehiculo, int(anio), int(kilometraje), float(precioCompra), float(precioVenta), estado)
            self.vehiculosDb.actualizarRegistro(vehiculoId, actualizarVehiculo.a_dict())
            print("Vehiculo actualizado exitosamente.")
        else:
            print("Vehiculo no encontrado.")

    def eliminarVehiculo(self):
        # Solicitar ID del vehiculo y eliminarlo
        vehiculoId = int(input("Ingrese el ID del vehiculo a eliminar: "))
        self.vehiculosDb.eliminarRegistro(vehiculoId)
        print("Vehiculo eliminado exitosamente.")

    def listarVehiculos(self):
        # Mostrar todos los vehiculos
        vehiculos = self.vehiculosDb.obtenerTodosLosRegistros()
        if vehiculos:
            # Imprimir encabezados de la tabla
            print("{:<5} {:<10} {:<10} {:<10} {:<15} {:<5} {:<12} {:<15} {:<15}".format(
                "ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta"
            ))
            print("=" * 100)
            #Imprimir cada vehiculo en formato de tabla
            for vehiculo in vehiculos:
                print("{:<5} {:<10} {:<10} {:<10} {:<15} {:<5} {:<12} {:<15} {:<15}".format(
                    vehiculo.get('id', 'N/A'),
                    vehiculo.get('placa', 'N/A'),
                    vehiculo.get('marca', 'N/A'),
                    vehiculo.get('modelo', 'N/A'),
                    vehiculo.get('tipoVehiculo', 'N/A'),
                    vehiculo.get('anio', 'N/A'),
                    vehiculo.get('kilometraje', 'N/A'),
                    vehiculo.get('precioCompra', 'N/A'),
                    vehiculo.get('precioVenta', 'N/A')
                ))
        else:
            print("No hay vehiculos registrados.")

        
    def listarClientes(self):
        # Mostrar todos los clientes en formato de tabla
        clientes = self.customDb.obtenerTodosLosRegistros()
        if clientes:
            # Obtener la longitud maxima de los datos para cada columna
            max_lengths = {
            "ID": max(len(str(cliente.get('id', 'N/A'))) for cliente in clientes),
            "Nombre": max(len(cliente.get('nombre', 'N/A')) for cliente in clientes),
            "Documento": max(len(str(cliente.get('documento', 'N/A'))) for cliente in clientes),
            "Apellido": max(len(cliente.get('apellido', 'N/A')) for cliente in clientes),
            "Direccion": max(len(cliente.get('direccion', 'N/A')) for cliente in clientes),
            "Celular": max(len(cliente.get('celular', 'N/A')) for cliente in clientes),
            "Email": max(len(cliente.get('email', 'N/A')) for cliente in clientes),
        }

        # Imprime los encabezados de las columnas
        print("{:<{id_width}} {:<{nombre_width}} {:<{doc_width}} {:<{apellido_width}} {:<{direccion_width}} {:<{celular_width}} {:<{email_width}}".format(
            "ID", "Nombre", "Documento", "Apellido", "Direccion", "Celular", "Email",
            id_width=max_lengths["ID"] + 2, nombre_width=max_lengths["Nombre"] + 2,
            doc_width=max_lengths["Documento"] + 2, apellido_width=max_lengths["Apellido"] + 2,
            direccion_width=max_lengths["Direccion"] + 2, celular_width=max_lengths["Celular"] + 2,
            email_width=max_lengths["Email"]
        ))
        print("=" * (sum(max_lengths.values()) + 12))  # Línea divisoria

        # Imprime los datos de los clientes
        for cliente in clientes:
            print("{:<{id_width}} {:<{nombre_width}} {:<{doc_width}} {:<{apellido_width}} {:<{direccion_width}} {:<{celular_width}} {:<{email_width}}".format(
                cliente.get('id', 'N/A'),
                cliente.get('nombre', 'N/A'),
                cliente.get('documento', 'N/A'),
                cliente.get('apellido', 'N/A'),
                cliente.get('direccion', 'N/A'),
                cliente.get('celular', 'N/A'),
                cliente.get('email', 'N/A'),
                id_width=max_lengths["ID"] + 2, nombre_width=max_lengths["Nombre"] + 2,
                doc_width=max_lengths["Documento"] + 2, apellido_width=max_lengths["Apellido"] + 2,
                direccion_width=max_lengths["Direccion"] + 2, celular_width=max_lengths["Celular"] + 2,
                email_width=max_lengths["Email"]
            ))
        else:
            print("No hay clientes registrados.")

    def administrarCustomers(self):
        # similar a modificarVehiculos
        while True:
            print("\n1. Crear Cliente")
            print("2. Editar Cliente")
            print("3. Eliminar Cliente")
            print("4. Listar Clientes")
            print("5. Volver al Menu Principal")
            choice = input("Seleccione una opcion: ")
            if choice == '1':
                self.crearCustomer()
            elif choice == '2':
                self.editarCustomer()
            elif choice == '3':
                self.eliminarCustomer()
            elif choice == '4':
                self.listarClientes()
            elif choice == '5':
                return
            else:
                print("Opcion invalida, por favor intente nuevamente.")

    def crearCustomer(self):
        nombre = input("Ingrese el nombre del cliente: ")
        documento = input("Ingrese el documento del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        direccion = input("Ingrese la direccion del cliente: ")
        celular = input("Ingrese el telefono del cliente: ")
        email = input("Ingrese el correo electronico del cliente: ")

        customerId = len(self.customDb.obtenerTodosLosRegistros()) + 1
        nuevoCustomer = Customer(customerId, nombre, documento, apellido, direccion, celular, email)
        self.customDb.agregarRegistro(nuevoCustomer.a_dict())
        print("Cliente creado exitosamente.")

    def editarCustomer(self):
        customerId = int(input("Ingrese el ID del cliente a editar: "))
        customer = self.customDb.buscarRegistrosPorId(customerId)
        if customer:
            print("Deje en blanco si no desea modificar el campo.")
            nombre = input(f"Nombre actual ({customer['nombre']}): ") or customer['nombre']
            documento = input(f"Documento actual ({customer['documento']}): ") or customer['documento']
            apellido = input(f"Apellido actual ({customer['apellido']}): ") or customer['apellido']
            direccion = input(f"Direccion actual ({customer['direccion']}): ") or customer['direccion']
            celular = input(f"Telefono actual ({customer['celular']}): ") or customer['celular']
            email = input(f"Correo electronico actual ({customer['email']}): ") or customer['email']

            actualizarCustomer = Customer(customerId, nombre, documento, apellido, direccion, celular, email)
            self.customDb.actualizarRegistro(customerId, actualizarCustomer.a_dict())
            print("Cliente actualizado exitosamente.")
        else:
            print("Cliente no encontrado.")

    def eliminarCustomer(self):
        customerId = int(input("Ingrese el ID del cliente a eliminar: "))
        self.customDb.eliminarRegistro(customerId)
        print("Cliente eliminado exitosamente.")

    def listaCustomers(self):
        customers = self.customDb.obtenerTodosLosRegistros()
        for customer in customers:
            print(customer)

    def administrarTransacciones(self):
        while True:
            print("\n1. Crear Transaccion")
            print("2. Listar Transacciones")
            print("3. Volver al Menu Principal")
            choice = input("Seleccione una opcion: ")
            if choice == '1':
                self.crearTransaccion()
            elif choice == '2':
                self.listarTransacciones()
            elif choice == '3':
                return
            else:
                print("Opcion invalida, por favor intente nuevamente.")

    def crearTransaccion(self):
        customerId = int(input("Ingrese el ID del cliente: "))
        vehiculoId = int(input("Ingrese el ID del vehiculo: "))
        precioVenta = float(input("Ingrese el precio de venta: "))

        transaccionId = len(self.transaccionesDb.obtenerTodosLosRegistros()) + 1
        nuevoTransaccion = Transaction(transaccionId, customerId, vehiculoId, precioVenta)
        self.transaccionesDb.agregarRegistro(nuevoTransaccion.a_dict())
        print("Transaccion registrada exitosamente.")

    def listarTransacciones(self):
        transacciones = self.transaccionesDb.obtenerTodosLosRegistros()
        for transaccion in transacciones:
            print(transaccion)


if __name__ == "__main__":
    interface = InterfazConcesionario()
    interface.mainMenu()
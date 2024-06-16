import sys
import os

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

    def limpiarPantalla(self):
        if os.name == 'nt':
            os.system('cls')  # Comando para Windows
        elif os.name == 'posix':
            os.system('clear')  #Comando para Mac/Linux
    
    def volverAtrasYSalir(self , subMenu , menu , texto):
        #Funcion 1 es el submenu, funcion 2 la principal, texto la opcion a evaluar
        opcion = input("Ingrese 1 para volver a " + texto + " 2 para ir al Menu Principal o Enter para salir: ").lower
        match opcion:
            case "1":
                elegida = subMenu
            case "2":
                elegida = menu
            case "":
                exit()
            case default:
                self.volverAtrasYSalir()
        return elegida

    def mainMenu(self):
        self.limpiarPantalla()
        choice = input("""
╔ =========== MENU =========== ╗
║  1. Gestionar Vehiculos      ║
║  2. Gestionar Clientes       ║
║  3. Registrar Transaccion    ║
║  4. Salir                    ║ 
╚ ============================ ╝
   Seleccione una opcion: """
                        )
        match choice:
            case '1':
                self.limpiarPantalla()
                self.modificarVehiculos()
            case '2':
                self.limpiarPantalla()
                self.administrarCustomers()
            case '3':
                self.limpiarPantalla()
                self.administrarTransacciones()
            case '4':
                self.limpiarPantalla()
                sys.exit()
            case default:
                print("  Opcion invalida, por favor intentelo nuevamente.")
                self.mainMenu()
   

    def modificarVehiculos(self):
        choice = input("""
╔ ============ MENU =========== ╗
║  1. Crear Vehiculo            ║
║  2. Editar Vehiculo           ║
║  3. Eliminar Vehiculo         ║
║  4. Listar Vehiculos          ║
║  5. Volver al menu principal  ║
╚ ============================= ╝
  Seleccione una opcion: """
                        )
        match choice:
            case '1':
                self.crearVehiculo()
            case '2':
                self.editarVehiculo()
            case '3':
                self.eliminarVehiculo()
            case '4':
                self.listarVehiculos()
            case '5':
                self.mainMenu()
            case default:
                print("  Opcion invalida, por favor intente nuevamente.")
                self.modificarVehiculos()

    def crearVehiculo(self):
        # Solicitar datos y crear el vehiculo
        patente = input("  Ingrese la patente del vehiculo: ")
        marca = input("  Ingrese la marca del vehiculo: ")
        modelo = input("  Ingrese el modelo del vehiculo: ")
        tipoVehiculo = input("  Ingrese el tipo del vehiculo (Sedán, SUV, Pick Up, etc): ")
        anio = int(input("  Ingrese el año del vehiculo: "))
        kilometraje = int(input("  Ingrese el kilometraje del vehiculo: "))
        precioCompra = float(input("  Ingrese el precio de compra del vehiculo: "))
        precioVenta = float(input("  Ingrese el precio de venta del vehiculo: "))
        estado = input("  Ingrese el estado del vehiculo (Disponible, Reservado, Vendido): ")
        vehiculoId = len(self.vehiculosDb.obtenerTodosLosRegistros()) + 1
        nuevoVehiculo = Vehicle(vehiculoId, patente, marca, modelo, tipoVehiculo, anio, kilometraje, precioCompra, precioVenta, estado)
        self.vehiculosDb.agregarRegistro(nuevoVehiculo.a_dict())
        print("  Vehiculo creado correctamente.")

        self.volverAtrasYSalir(self.modificarVehiculos(), self.mainMenu(),"Ingrese 1 para volver a modificar vehiculos o 2 para volver al menu principal")

    def editarVehiculo(self):
        # Solicitar ID del vehículo y editar los datos
        vehiculoId = int(input("  Ingrese el ID del vehiculo a editar: "))
        vehiculo = self.vehiculosDb.buscarRegistrosPorId(vehiculoId)
        if vehiculo:
            print("  Deje en blanco si no desea modificar el campo.")
            patente = input(f"  Patente actual ({vehiculo['patente']}): ") or vehiculo['patente']
            marca = input(f"  Marca actual ({vehiculo['marca']}): ") or vehiculo['marca']
            modelo = input(f"  Modelo actual ({vehiculo['modelo']}): ") or vehiculo['modelo']
            tipoVehiculo = input(f"  Tipo actual ({vehiculo['tipo']}): ") or vehiculo['tipo']
            anio = input(f"  Año actual ({vehiculo['anio']}): ") or vehiculo['anio']
            kilometraje = input(f"  Kilometraje actual ({vehiculo['kilometraje']}): ") or vehiculo['kilometraje']
            precioCompra = input(f"Precio de compra actual ({vehiculo['precioCompra']}): ") or vehiculo['precioCompra']
            precioVenta = input(f"Precio de venta actual ({vehiculo['precioVenta']}): ") or vehiculo['precioVenta']
            estado = input(f"  Estado actual ({vehiculo['estado']}): ") or vehiculo['estado']

            actualizarVehiculo = Vehicle(vehiculoId, patente, marca, modelo, tipoVehiculo, int(anio), int(kilometraje), float(precioCompra), float(precioVenta), estado)
            self.vehiculosDb.actualizarRegistro(vehiculoId, actualizarVehiculo.a_dict())
            print("  Vehiculo actualizado exitosamente.")
        else:
            print("  Vehiculo no encontrado.")
        self.volverAtrasYSalir(self.modificarVehiculos(), self.mainMenu(), "Ingrese 1 para volver a modificar vehiculos o 2 para volver al menu principal" )

    def eliminarVehiculo(self):
        # Solicitar ID del vehiculo y eliminarlo
        vehiculoId = int(input("  Ingrese el ID del vehiculo a eliminar: "))
        self.vehiculosDb.eliminarRegistro(vehiculoId)
        print("  Vehiculo eliminado exitosamente.")
        self.volverAtrasYSalir(self.modificarVehiculos(), self.mainMenu() ,"Ingrese 1 para volver a modificar vehiculos o 2 para volver al menu principal")

    def listarVehiculos(self):
        # Mostrar todos los vehiculos
        vehiculos = self.vehiculosDb.obtenerTodosLosRegistros()
        if vehiculos:
            print("╔ ============================================================================================================================ ╗")
            # Imprimir encabezados de la tabla
            print("║ {:<5}║ {:<10}║ {:<15}║ {:<16}║ {:<15}║ {:<5}║ {:<12}║ {:<15}║ {:<12}    ║".format(
                "ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta"
            ))
            print("=" * 128)
            #Imprimir cada vehiculo en formato de tabla
            for vehiculo in vehiculos:
                print("║ {:<5}║ {:<10}║ {:<15}║ {:<16}║ {:<15}║ {:<5}║ {:<12}║ {:<15}║ {:<12}    ║".format(
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
            print("╚ ============================================================================================================================ ╝")
            print("No hay vehiculos registrados.")
        else:
            self.volverAtrasYSalir(self.modificarVehiculos(), self.mainMenu(),"Ingrese 1 para volver a modificar vehiculos o 2 para volver al menu principal")
        
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

        print("╔ =========================================================================================================== ╗")
        # Imprime los encabezados de las columnas
        print("║ {:<{id_width}}║ {:<{nombre_width}}║ {:<{doc_width}}║ {:<{apellido_width}}║ {:<{direccion_width}}║ {:<{celular_width}}║ {:<{email_width}}    ║".format(
            "ID", "Nombre", "Documento", "Apellido", "Direccion", "Celular", "Email",
            id_width=max_lengths["ID"] + 2, nombre_width=max_lengths["Nombre"] + 2,
            doc_width=max_lengths["Documento"] + 2, apellido_width=max_lengths["Apellido"] + 2,
            direccion_width=max_lengths["Direccion"] + 2, celular_width=max_lengths["Celular"] + 2,
            email_width=max_lengths["Email"]
        ))
        print("=" * (sum(max_lengths.values()) + 30))  # Línea divisoria

        # Imprime los datos de los clientes
        for cliente in clientes:
            print("║ {:<{id_width}}║ {:<{nombre_width}}║ {:<{doc_width}}║ {:<{apellido_width}}║ {:<{direccion_width}}║ {:<{celular_width}}║ {:<{email_width}}    ║".format(
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
            print("╚ =========================================================================================================== ╝")
            print("  No hay clientes registrados.")
        self.volverAtrasYSalir(self.modificarVehiculos(), self.mainMenu(),"Ingrese 1 para volver a modificar vehiculos o 2 para volver al menu principal")

    def administrarCustomers(self):
        # similar a modificarVehiculos
        choice = input("""
╔ ============ MENU =========== ╗
║  1. Crear Cliente             ║
║  2. Editar Cliente            ║
║  3. Eliminar Cliente          ║
║  4. Listar Clientes           ║
║  5. Volver al Menu Principal  ║
╚ ============================= ╝
   Seleccione una opcion: """
                        )
        match choice:
            case '1':
                self.crearCustomer()
            case '2':
                self.editarCustomer()
            case '3':
                self.eliminarCustomer()
            case '4':
                self.listarClientes()
            case '5':
                return
            case default:
                print("  Opcion invalida, por favor intente nuevamente.")
            #   Aca hay q llamar denuevo a la función, pero creo que seria desde main, nose como xD

    def crearCustomer(self):
        nombre = input("  Ingrese el nombre del cliente: ")
        documento = input("  Ingrese el documento del cliente: ")
        apellido = input("  Ingrese el apellido del cliente: ")
        direccion = input("  Ingrese la direccion del cliente: ")
        celular = input("  Ingrese el telefono del cliente: ")
        email = input("  Ingrese el correo electronico del cliente: ")

        customerId = len(self.customDb.obtenerTodosLosRegistros()) + 1
        nuevoCustomer = Customer(customerId, nombre, documento, apellido, direccion, celular, email)
        self.customDb.agregarRegistro(nuevoCustomer.a_dict())
        print("  Cliente creado exitosamente.")

    def editarCustomer(self):
        customerId = int(input("  Ingrese el ID del cliente a editar: "))
        customer = self.customDb.buscarRegistrosPorId(customerId)
        if customer:
            print("  Deje en blanco si no desea modificar el campo.")
            nombre = input(f"  Nombre actual ({customer['nombre']}): ") or customer['nombre']
            documento = input(f"  Documento actual ({customer['documento']}): ") or customer['documento']
            apellido = input(f"  Apellido actual ({customer['apellido']}): ") or customer['apellido']
            direccion = input(f"  Direccion actual ({customer['direccion']}): ") or customer['direccion']
            celular = input(f"  Telefono actual ({customer['celular']}): ") or customer['celular']
            email = input(f"  Correo electronico actual ({customer['email']}): ") or customer['email']

            actualizarCustomer = Customer(customerId, nombre, documento, apellido, direccion, celular, email)
            self.customDb.actualizarRegistro(customerId, actualizarCustomer.a_dict())
            print("  Cliente actualizado exitosamente.")
        else:
            print("  Cliente no encontrado.")

    def eliminarCustomer(self):
        customerId = int(input("Ingrese el ID del cliente a eliminar: "))
        self.customDb.eliminarRegistro(customerId)
        print("  Cliente eliminado exitosamente.")

    def listaCustomers(self):
        customers = self.customDb.obtenerTodosLosRegistros()
        for customer in customers:
            print(customer)

    def administrarTransacciones(self):
        choice = input("""
╔ =========== MENU ============ ╗
║  1. Crear Transaccion         ║
║  2. Listar Transacciones      ║
║  3. Volver al Menu Principal  ║
╚ ============================= ╝  
   Seleccione una opcion: """
                  )
        match choice:
            case '1':
                self.crearTransaccion()
            case '2':
                self.listarTransacciones()
            case '3':
                return
            case default:
                print("Opcion invalida, por favor intente nuevamente.")
            #   Aca hay q llamar denuevo a la función, pero creo que seria desde main, nose como xD

    def crearTransaccion(self):
        customerId = int(input("  Ingrese el ID del cliente: "))
        vehiculoId = int(input("  Ingrese el ID del vehiculo: "))
        precioVenta = float(input("  Ingrese el precio de venta: "))

        transaccionId = len(self.transaccionesDb.obtenerTodosLosRegistros()) + 1
        nuevoTransaccion = Transaction(transaccionId, customerId, vehiculoId, precioVenta)
        self.transaccionesDb.agregarRegistro(nuevoTransaccion.a_dict())
        print("  Transaccion registrada exitosamente.")

    def listarTransacciones(self):
        transacciones = self.transaccionesDb.obtenerTodosLosRegistros()
        for transaccion in transacciones:
            print(transaccion)


if __name__ == "__main__":
    interface = InterfazConcesionario()
    interface.mainMenu()
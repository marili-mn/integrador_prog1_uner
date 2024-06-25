import sys
import os

from vehiculos import Vehiculos
from clientes import Clientes
from transaccion import Transaccion
from database import Database
from prettytable import PrettyTable
#pip install prettytable
#   Importamos las clases de los json

global resultados
resultados = []

class InterfazConcesionario:
    def __init__(self):
        self.vehiculosDb = Database('data/vehiculos.json')
        self.clientesDb = Database('data/clientes.json')
        self.transaccionesDb = Database('data/transacciones.json')

    def limpiarPantalla(self):
        if os.name == 'nt':
            os.system('cls')  # Comando para Windows
        elif os.name == 'posix':
            os.system('clear')  #Comando para Mac/Linux

    def volverAtrasYSalir(self, subMenu, texto):
        while True:
            opcion = input(f"""
╔ ========================== MENU ========================== ╗              
║   Ingrese 1 para volver a {texto}      ║
║   Ingrese 2 para ir al Menú Principal                      ║
║   Enter para salir                                         ║
╚ ========================================================== ╝
    Ingrese una opción: """ 
              ).strip().lower()
            if opcion == "1":
                subMenu()
                break
            elif opcion == "2":
                self.mainMenu()
                break
            elif opcion == "":
                sys.exit()
            else:
                print("  Opción inválida, por favor inténtelo nuevamente.")
#################################
#################################
    def mainMenu(self):        ##
        choice = ""
        self.limpiarPantalla()
        choice = input("""
╔ ========================== MENU ========================== ╗
║  1. Gestionar Vehículos                                    ║
║  2. Gestionar Clientes                                     ║
║  3. Gestionar Transacciones                                ║
║  4. Salir                                                  ║ 
╚ ========================================================== ╝
   Seleccione una opcion: """  ##
                        )
        match choice:
            case '1':
                self.limpiarPantalla()
                self.gestionarVehiculos()
            case '2':
                self.limpiarPantalla()
                self.gestionarClientes()
            case '3':
                self.limpiarPantalla()
                self.gestionarTransacciones()
            case '4':
                self.limpiarPantalla()
                sys.exit()
            case default:
                print("  Opción invalida, por favor inténtelo nuevamente.")
                self.mainMenu()
#################################
#################################
    def gestionarVehiculos(self):
        opcion = input("""
╔ ========================== MENU ========================== ╗
║  1. Crear Vehículo                                         ║
║  2. Editar Vehículo                                        ║
║  3. Eliminar Vehículo                                      ║
║  4. Listar Vehículos                                       ║
║  5. Buscar Vehículos                                       ║
║  6. Volver al Menú Principal                               ║
╚ ========================================================== ╝
  Seleccione una opción: """
                        )
        match opcion:
            case '1':
                self.limpiarPantalla()
                self.crearVehiculo()
            case '2':
                self.limpiarPantalla()
                self.editarVehiculo()
            case '3':
                self.limpiarPantalla()
                self.eliminarVehiculo()
            case '4':
                self.limpiarPantalla()
                self.listarVehiculos()
            case '5':
                self.limpiarPantalla()
                self.buscadorVehiculos()
            case '6':
                self.limpiarPantalla()
                self.mainMenu()
            case default:
                print("  Opción invalida, por favor intente nuevamente.")
                self.gestionarVehiculos()
#################################
#################################
    def crearVehiculo(self):   ##

        # Solicitar datos y crear el vehiculo
        try:

            patente = input("  Ingrese la patente del vehículo: ").upper()
            marca = input("  Ingrese la marca del vehículo: ").capitalize()
            modelo = input("  Ingrese el modelo del vehículo: ").capitalize()
            tipo_vehiculo = input("  Ingrese el tipo del vehiculo (Sedán, SUV, Pick Up, etc): ").capitalize()
            anio = int(input("  Ingrese el año del vehículo: "))
            kilometraje = input("  Ingrese el kilometraje del vehículo: ").strip()
            precio_compra = float(input("  Ingrese el precio de compra del vehículo: "))
            precio_venta = float(input("  Ingrese el precio de venta del vehículo: "))
            estado = input("  Ingrese el estado del vehículo (Disponible, Reservado, Vendido): ").strip().capitalize()

        except ValueError:
            self.limpiarPantalla()
            print("  Precio de compra, precio de venta y año deben ingresarse en formato numérico")
            print("  Ingrese los datos del vehículo nuevamente: ")
            self.crearVehiculo()

        item_id = len(self.vehiculosDb.obtenerTodosLosRegistros()) + 1
        nuevoVehiculo = Vehiculos(item_id, patente, marca, modelo, tipo_vehiculo, anio, kilometraje, precio_compra, precio_venta, estado)
        self.vehiculosDb.agregarRegistro(nuevoVehiculo.a_dict())
        self.limpiarPantalla()
        print("  Vehículo creado correctamente.")
        self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos    ")
#################################
#################################            
    def editarVehiculo(self):  ##
        # Solicitar ID del vehículo y editar los datos
        item_id = int(input("  Ingrese el ID del vehículo a editar: "))
        vehiculo = self.vehiculosDb.buscarRegistrosPorId(item_id)
        if vehiculo:
            try:

                print("  Deje en blanco si no desea modificar el campo.")
                patente = input(f"  Patente actual ({vehiculo['patente']}): ").upper() or vehiculo['patente']
                marca = input(f"  Marca actual ({vehiculo['marca']}): ").capitalize() or vehiculo['marca']
                modelo = input(f"  Modelo actual ({vehiculo['modelo']}): ").capitalize() or vehiculo['modelo']
                tipo_vehiculo = input(f"  Tipo actual ({vehiculo['tipo_vehiculo']}): ").capitalize() or vehiculo['tipo_vehiculo']
                anio = int(input(f"  Año actual ({vehiculo['anio']}): ") or vehiculo['anio'])
                kilometraje = input(f"  Kilometraje actual ({vehiculo['kilometraje']}): ").strip() or vehiculo['kilometraje']
                precio_compra = float(input(f"  Precio de compra actual ({vehiculo['precio_compra']}): ") or vehiculo['precio_compra'])
                precio_venta = float(input(f"  Precio de venta actual ({vehiculo['precio_venta']}): ") or vehiculo['precio_venta'])
                estado = input(f"  Estado actual ({vehiculo['estado']}): ").strip().capitalize() or vehiculo['estado']

            except ValueError:
                self.limpiarPantalla()
                print("  Precio de compra, precio de venta y año deben ingresarse en formato numérico")
                print("  Ingrese los datos del vehículo nuevamente: ")
                self.editarVehiculo()

            actualizarVehiculo = Vehiculos(item_id, patente, marca, modelo, tipo_vehiculo, int(anio), int(kilometraje), float(precio_compra), float(precio_venta), estado)
            self.vehiculosDb.actualizarRegistro(item_id, actualizarVehiculo.a_dict())
            print("  Vehículo actualizado exitosamente.")
        else:
            print("  Vehículo no encontrado.")
        self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos    ")
#################################
#################################
    def eliminarVehiculo(self):##
        # Solicitar ID del vehiculo y eliminarlo
        try:
            item_id = int(input("  Ingrese el ID del vehículo a eliminar: "))
            self.vehiculosDb.eliminarRegistro(item_id)
            print("  Vehículo eliminado exitosamente.")
            self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos    ")
        except ValueError:
            self.limpiarPantalla()
            print("El ID del vehículo debe ser un número")
            self.eliminarVehiculo()
#################################
#################################
    def listarVehiculos(self): ##
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
                    vehiculo.get('item_id', 'N/A'),
                    vehiculo.get('patente', 'N/A'),
                    vehiculo.get('marca', 'N/A'),
                    vehiculo.get('modelo', 'N/A'),
                    vehiculo.get('tipo_vehiculo', 'N/A'),
                    vehiculo.get('anio', 'N/A'),
                    vehiculo.get('kilometraje', 'N/A'),
                    vehiculo.get('precio_compra', 'N/A'),
                    vehiculo.get('precio_venta', 'N/A')
                ))
            print("╚ ============================================================================================================================ ╝")
        else:
            print("No hay vehículos registrados.")
        self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de Vehículos    ")
#################################
#################################
    def buscadorVehiculos (self):       ##
        parametros = ["patente", "marca", "modelo", "precio_compra", "precio_venta", "estado"]
        contador =len(parametros)
        entrada = ""    #input
        #print(" =============== MENU ============ ")
        resultados = None
        print(" =============== MENU ============ ")
        for i in range(contador):
            a = ("\n " + "  " + str(i+1)+ ". " + "{:27}".format((str(parametros[i]).capitalize())) + "║")
           # a = ("\n " + " ║  " + str(i+1)+ ". " + "{:27}".format((str(parametros[i]).capitalize())) + "║")
            entrada += a       
        #####
        opcion = input(entrada + "" + "\n   " + str(len(parametros)+1) + ". Volver al menu principal   ║" + "\n" + "    Seleccione una opción:       ║")
       # opcion = input(" ║" + "{:28}".format(" ") + "║" + "\n"+ "║" + entrada + "\n║   " + str(len(parametros)+1) + ". Volver al menu principal    ║" + "\n" + "    Seleccione una opción:    ")
        if opcion.isdigit():
            caso = int(opcion)-1
            if caso < len(parametros):
                    buscar = input("  Ingrese " + parametros[caso]+ ": ")
                    if caso == -1:
                        caso=0
                    resultados= self.vehiculosDb.buscarRegistrosPorParametro(buscar, parametros[caso])
                    if resultados ==[]:
                        print("  No se encontró ningún vehículo con esos parámetros.")
            elif caso == len(parametros):
                self.mainMenu()
        else:
            print(" ================================= ")
            print("  Opción inválida, por favor inténtelo nuevamente.")
            input("  Presione Cualquier tecla para continuar...")
            self.limpiarPantalla()
            self.buscadorVehiculos()
        #if resultados:
        if resultados is not None:
            for resultado in resultados:
                    print("╔ ============================================================================================================================================== ╗")
                    print("║ {:<5}║ {:<10}║ {:<15}║ {:<16}║ {:<15}║ {:<5}║ {:<12}║ {:<15}║ {:<12}║ {:<12}        ║".format(
                        "ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta", "Estado"
                    ))
                    print("=" * 146)
                        #Imprimir cada vehiculo en formato de tabla
                    print("║ {:<5}║ {:<10}║ {:<15}║ {:<16}║ {:<15}║ {:<5}║ {:<12}║ {:<15}║ {:<12}║ {:<12}        ║".format(
                            resultado.get('item_id' , 'N/A'),
                            resultado.get('patente' , 'N/A'),
                            resultado.get('marca' , 'N/A'),
                            resultado.get('modelo' , 'N/A'),
                            resultado.get('tipo_vehiculo' , 'N/A'),
                            resultado.get('anio' , 'N/A'),
                            resultado.get('kilometraje' , 'N/A'),
                            resultado.get('precio_compra' , 'N/A'),
                            resultado.get('precio_venta' , 'N/A'),
                            resultado.get('estado' , 'N/A')
                        ))
                    print("╚ ============================================================================================================================================== ╝")
        else:
            print("  No se encontraron resultados para su búsqueda.")
        input("  Presione Cualquier tecla para continuar...")
        self.limpiarPantalla()           
        self.volverAtrasYSalir(self.buscadorVehiculos(), "Menú Principal")
#################################
#################################
    def gestionarClientes(self):#
        choice = input("""     
╔ ========================== MENU ========================== ╗
║  1. Crear Cliente                                          ║
║  2. Editar Cliente                                         ║
║  3. Eliminar Cliente                                       ║
║  4. Listar Clientes                                        ║
║  5. Volver al Menu Principal                               ║
╚ ========================================================== ╝
   Seleccione una opcion: """  ##
                        )
        match choice:
            case '1':
                self.crearCliente()
            case '2':
                self.editarClientes()
            case '3':
                self.eliminarClientes()
            case '4':
                self.listarClientes()
            case '5':
                self.mainMenu()
            case default:
                print("  Opción invalida, por favor intente nuevamente.")
                self.gestionarClientes()
#################################
#################################                
    def crearCliente(self):    ##
        nombre = input("  Ingrese el nombre del cliente: ").capitalize()
        documento = input("  Ingrese el documento del cliente: ").strip()
        apellido = input("  Ingrese el apellido del cliente: ").capitalize()
        direccion = input("  Ingrese la direccion del cliente: ").capitalize()
        celular = input("  Ingrese el telefono del cliente: ").strip()
        email = input("  Ingrese el correo electronico del cliente: ").strip().lower()

        item_id = len(self.clientesDb.obtenerTodosLosRegistros()) + 1
        nuevoCliente = Clientes(item_id, nombre, documento, apellido, direccion, celular, email)
        self.clientesDb.agregarRegistro(nuevoCliente.a_dict())
        print("  Cliente creado exitosamente.")
        self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes     ")
#################################
#################################
    def editarClientes(self):  ##
        
        try:
            item_id = int(input("  Ingrese el ID del cliente a editar: "))
        except ValueError:
            
            self.limpiarPantalla()
            print("El ID del cliente a editar debe ser un número")
            print("Intentelo otra vez")
            self.editarClientes()

        cliente = self.clientesDb.buscarRegistrosPorId(item_id)
        if cliente:
            print("  Deje en blanco si no desea modificar el campo.")
            nombre = input(f"  Nombre actual ({cliente['nombre']}): ").capitalize() or cliente['nombre']
            documento = input(f"  Documento actual ({cliente['documento']}): ").strip() or cliente['documento']
            apellido = input(f"  Apellido actual ({cliente['apellido']}): ").capitalize() or cliente['apellido']
            direccion = input(f"  Direccion actual ({cliente['direccion']}): ") or cliente['direccion']
            celular = input(f"  Telefono actual ({cliente['celular']}): ").strip() or cliente['celular']
            email = input(f"  Correo electronico actual ({cliente['email']}): ").strip().lower() or cliente['email']

            actualizarCliente = Clientes(item_id, nombre, documento, apellido, direccion, celular, email)
            self.clientesDb.actualizarRegistro(item_id, actualizarCliente.a_dict())
            print("  Cliente actualizado exitosamente.")
        else:
            print("  Cliente no encontrado.")
            self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes     ")
#################################
#################################
    def eliminarClientes(self):##
        try:

            item_id = int(input("Ingrese el ID del cliente a eliminar: "))
            self.clientesDb.eliminarRegistro(item_id)
            print("  Cliente eliminado exitosamente.")
        except ValueError:
            self.limpiarPantalla()
            print("El ID del cliente debe ser un número")
            print("Intentelo otra vez")
            self.eliminarClientes()

        self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes     ")
#################################
#################################
    def listarClientes(self):  ##
        # Mostrar todos los clientes en formato de tabla
        clientes = self.clientesDb.obtenerTodosLosRegistros()
        if clientes:
            # Obtener la longitud maxima de los datos para cada columna
            max_lengths = {
            "ID": max(len(str(cliente.get('item_id', 'N/A'))) for cliente in clientes),
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
            print("=" * (sum(max_lengths.values()) + 31))  # Línea divisoria

            # Imprime los datos de los clientes
            for cliente in clientes:
                print("║ {:<{id_width}}║ {:<{nombre_width}}║ {:<{doc_width}}║ {:<{apellido_width}}║ {:<{direccion_width}}║ {:<{celular_width}}║ {:<{email_width}}    ║".format(
                    cliente.get('item_id', 'N/A'),
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
                print("╚ =========================================================================================================== ╝")
        else:    
            print("  No hay clientes registrados.")
        self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes     ")
#################################
#################################
    def gestionarTransacciones(self):
        choice = input("""
╔ ========================== MENU ========================== ╗
║  1. Crear Transacción                                      ║
║  2. Listar Transacciones                                   ║
║  3. Volver al Menú Principal                               ║
╚ ========================================================== ╝ 
   Seleccione una opcion: """
                  )
        match choice:
            case '1':
                self.crearTransaccion()
            case '2':
                self.listarTodasLasTransacciones()
            case '3':
                self.mainMenu()
            case default:
                print("  Opción invalida, por favor intente nuevamente.")
                self.gestionarTransacciones()
#################################
#################################
    def crearTransaccion(self):##

        try:
            id_vehiculo = int(input("  Ingrese el ID del vehículo: "))
            id_cliente = int(input("  Ingrese el ID del cliente: "))
            tipo_transaccion = input("  Ingrese el tipo de transacción(compra o venta) : ").capitalize().strip()
            fecha = input("  Ingrese la fecha de la transacción (YYYY-MM-DD): ").strip()
            monto = float(input("  Ingrese el monto de la transacción: "))
            observaciones = input("  Ingrese las observaciones de la transacción: ").capitalize()
        except ValueError:
            self.limpiarPantalla()
            print("  Los datos ingresados deben ser valores numeros ")
            print("  Ingrese los datos de la transacción nuevamente: ")
            self.crearTransaccion()
        
        item_id = len(self.transaccionesDb.obtenerTodosLosRegistros()) + 1
        nuevoTransaccion = Transaccion(item_id, id_vehiculo, id_cliente, tipo_transaccion, fecha, monto, observaciones)
        self.transaccionesDb.agregarRegistro(nuevoTransaccion.a_dict())
        print("  Transacción registrada exitosamente.")
        self.volverAtrasYSalir(self.gestionarTransacciones, "el SubMenú de Transacciones")
#################################
#################################
    def listarTodasLasTransacciones(self):
        # Mostrar todas las transacciones en formato de tabla
        transacciones = self.transaccionesDb.obtenerTodosLosRegistros()
        if transacciones:
            table = PrettyTable()
            table.field_names = ["ID Transacción", "ID Vehículo", "ID Cliente", "Transacción", "Fecha", "Monto", "Observaciones"]
            for transaccion in transacciones:
                table.add_row([
                    transaccion.get('item_id'),
                    transaccion.get('id_vehiculo'),
                    transaccion.get('id_cliente'),
                    transaccion.get('tipo_transaccion'),
                    transaccion.get('fecha'),
                    transaccion.get('monto'),
                    transaccion.get('observaciones')
                ])
            print(table)
        else:
            print("No hay transacciones registradas.")
        self.volverAtrasYSalir(self.gestionarTransacciones, "el SubMenú de Transacciones")
#################################
#################################
if __name__ == "__main__":     ##
    interface = InterfazConcesionario()
    interface.mainMenu()       ##
#################################
#################################
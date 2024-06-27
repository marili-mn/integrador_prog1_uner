import sys
import os
from prettytable import PrettyTable
from datetime import datetime
#librerías de pyhton

from vehiculos import Vehiculos
from clientes import Clientes
from transaccion import Transaccion
from database import Database
# 



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

    def tablas(self, ancho, registros:list, cabecera:list):
        #ancho se define como: "{:<38}" donde 38 es el ancho de la columna
        if (registros):
            for elemento in cabecera:
                table = PrettyTable()    
            table.field_names = ["  " +ancho.format(elemento)]
            
            for elemento in registros:
                table.add_row([ancho.format(elemento)])
            print(table)

    def tablas_diccionario (self, lista_cabecera:list, lista_diccionarios:list, ordenamiento, subMenu, texto):
        #ancho se define como: "{:<38}" donde 38 es el ancho de la columna
        if (lista_diccionarios):
            table = PrettyTable()    
            table.field_names = lista_cabecera
            for diccionario in lista_diccionarios:
                lista_string = list(diccionario.values())
                for i in range(len(lista_string)):
                    lista_string[i] = str(lista_string[i])
                table.add_row(lista_string)
            table.align = "l"
            table.sortby = ordenamiento
            print(table)
        input("  Presione Cualquier tecla para continuar...")
        self.limpiarPantalla()
        self.volverAtrasYSalir(subMenu, texto)        

    def volverAtrasYSalir(self, subMenu, texto):
        self.limpiarPantalla()
        string = "1. Volver a " + texto
        menu = [string, '2. Ir al Menú Principal', '3. Salir']
        self.tablas( "{:<42}", menu ,['MENU'])
        while True:
            opcion = input("Ingrese una opción:" ).strip().lower()
            if opcion == "1":
                self.limpiarPantalla()
                subMenu()
                break
            elif opcion == "2":
                self.limpiarPantalla()
                self.mainMenu()
                break
            elif opcion == "3":
                sys.exit()
            else:
                print("  Opción inválida, por favor inténtelo nuevamente.")
#################################
#################################
    def validarFechas(self, fecha, funcion_volver_a_menu):
        try:
            fecha_ok = datetime.fromisoformat(fecha)
            fecha = fecha_ok.strftime("%Y-%m-%d")
        except ValueError:
            print("Ingrese la fecha en el formato correcto (YYYY-MM-DD)")
            input("  Presione Cualquier tecla para continuar...")
            self.limpiarPantalla()
            funcion_volver_a_menu()
#################################
#################################
    def buscarEnMemoriaPorParametro(self,registroId, dic_operacion, parametro):
        coleccion =[]
        for registro in dic_operacion:
            if registro.get(parametro) == registroId:
                coleccion.append(registro)
        return coleccion
#################################
    def mainMenu(self):        ##
        choice = ""
        self.limpiarPantalla()
        menu = ['1. Vehículos', '2. Clientes', '3. Transacciones', '4. Salir']
        self.tablas("{:<28}", menu ,['  MENU PRINCIPAL'])
        choice = input()
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
                self.limpiarPantalla()
                self.mainMenu()
#################################
#################################
    def gestionarVehiculos(self):
        menu = ['1. Crear Vehículos', '2. Editar Vehículos', '3. Eliminar Vehículo', '4. Listar Vehículo', '5. Buscar Vehículo','6. Volver al Menú Principal']
        self.tablas("{:<28}",menu,['  MENU DE VEHICULOS'])
        opcion = input("")
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
                self.limpiarPantalla()
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
        self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos")
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
        self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos")
#################################
#################################
    def eliminarVehiculo(self):##
        # Solicitar ID del vehiculo y eliminarlo
        try:
            item_id = int(input("  Ingrese el ID del vehículo a eliminar: "))
            self.vehiculosDb.eliminarRegistro(item_id)
            print("  Vehículo eliminado exitosamente.")
            self.volverAtrasYSalir(self.gestionarVehiculos, "el SubMenú de vehículos")
        except ValueError:
            self.limpiarPantalla()
            print("El ID del vehículo debe ser un número")
            self.eliminarVehiculo()
#################################
#################################
    def listarVehiculos(self): ##
        # Mostrar todos los vehiculos
        vehiculos = self.vehiculosDb.obtenerTodosLosRegistros()
        cabecera = ["ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta", "Estado"]
        self.tablas_diccionario (cabecera, vehiculos,"Estado", self.gestionarVehiculos, "el SubMenú de vehículos")
#################################
#################################
    def buscadorVehiculos (self):       ##
        parametros = ["patente", "marca", "modelo", "precio_compra", "precio_venta", "estado"]
        menu = ["1. Patente", "2. Marca", "3. Modelo", "4. Precio_compra", "5. Precio_venta", "6. Estado"]
        contador =len(parametros)
        self.tablas("{:28}", menu, ["Buscador de vehículos"])
        opcion = input("  Opción:")
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
            print("  Opción inválida, por favor inténtelo nuevamente.")
            input("  Presione Cualquier tecla para continuar...")
            self.limpiarPantalla()
            self.buscadorVehiculos()
        self.limpiarPantalla()
        #if resultados:
        cabecera = ["ID", "Patente", "Marca", "Modelo", "Tipo", "Año", "Kilometraje", "Precio Compra", "Precio Venta", "Estado"]
        self.tablas_diccionario (cabecera, resultados,"Estado", self.gestionarVehiculos, "el SubMenú de vehículos")
#################################
#################################
    def gestionarClientes(self):#
        menu = ["1. Crear Cliente", "2. Editar Cliente", "3. Eliminar Cliente", "4. Listar Clientes", "5. Buscar Clientes", "6. Volver al Menu Principal"]
        self.tablas("{:38}",menu, ['MENU DE CLIENTES'])
        choice = input("")      #
        match choice:
            case '1':
                self.limpiarPantalla()
                self.crearCliente()
            case '2':
                self.limpiarPantalla()
                self.editarClientes()
            case '3':
                self.limpiarPantalla()
                self.eliminarClientes()
            case '4':
                self.limpiarPantalla()
                self.listarClientes()
            case '5':
                self.limpiarPantalla()
                self.buscadorClientes()
            case '6':
                self.limpiarPantalla()
                self.mainMenu()
            case default:
                self.limpiarPantalla()
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
        self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes")
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
            self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes")
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

        self.volverAtrasYSalir(self.gestionarClientes, "el SubMenú de Clientes")
#################################
#################################
    def listarClientes(self):  ##
        clientes = self.clientesDb.obtenerTodosLosRegistros()
        cabecera = ["ID", "Nombre", "Documento", "Apellido", "Direccion", "Celular", "Email"]
        self.tablas_diccionario(cabecera, clientes,"Documento", self.gestionarClientes, "el SubMenú de Clientes")
#################################
#################################
    def buscadorClientes (self):       ##
        parametros = ["documento", "apellido", "nombre"]
        menu = ["1. Documento", "2. Apellido", "3. Nombre"]
        contador =len(parametros)
        self.tablas("{:28}", menu, ["Buscador de clientes"])
        opcion = input("  Opción:")
        if opcion.isdigit():
            caso = int(opcion)-1
            if caso < len(parametros):
                    buscar = input("  Ingrese " + parametros[caso]+ ": ")
                    if caso == -1:
                        caso=0
                    resultados= self.clientesDb.buscarRegistrosPorParametro(buscar, parametros[caso])
                    print(resultados)
                    if resultados ==[]:
                        print("  No se encontró ningún Clientes con esos datos.")
            elif caso == len(parametros):
                self.mainMenu()
        else:
            print("  Opción inválida, por favor inténtelo nuevamente.")
            input("  Presione Cualquier tecla para continuar...")
            self.limpiarPantalla()
            self.buscadorClientes()
        self.limpiarPantalla()
        cabecera = ["ID", "Nombre", "Apellido","Documento", "Dirección", "Celular", "Email"]
        self.tablas_diccionario (cabecera, resultados,"ID", self.gestionarClientes, "el SubMenú de clientes")
#################################
#################################
    def gestionarTransacciones(self):
        menu = ["1. Crear Transacción", "2. Listar Transacciones","3. Buscar Transacción", "4. Volver al Menú Principal"]
        self.tablas("{:<28}",menu, ['MENU DE TRANSACCIONES'])
        choice = input("")
        match choice:
            case '1':
                self.limpiarPantalla()
                self.crearTransaccion()
            case '2':
                self.limpiarPantalla()
                self.listarTodasLasTransacciones()
            case '3':
                self.limpiarPantalla()
                self.buscadorTransacciones()    
            case '4':
                self.limpiarPantalla()
                self.mainMenu()
            case default:
                self.limpiarPantalla()
                self.gestionarTransacciones()
#################################
#################################
    def crearTransaccion(self):##

        try:
            id_vehiculo = int(input("  Ingrese el ID del vehículo: "))
            id_cliente = int(input("  Ingrese el ID del cliente: "))
            tipo_transaccion = input("  Ingrese el tipo de transacción(compra o venta) : ").capitalize().strip()
            ####
            fecha = input("  Ingrese la fecha de la transacción (YYYY-MM-DD): ").strip()
            self.validarFechas(fecha, self.crearTransaccion)
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
        cabecera = ["ID Transacción", "ID Vehículo", "ID Cliente", "Transacción", "Fecha", "Monto", "Observaciones"]
        transacciones = self.transaccionesDb.obtenerTodosLosRegistros()
        self.tablas_diccionario (cabecera, transacciones,"Fecha", self.gestionarTransacciones, "el SubMenú de Transacciones")
#################################
#################################
    def buscadorTransacciones(self):
        menu = ["1. Buscar por compras", "2. Buscar por ventas"]
        self.tablas("{:<48}", menu, ["Buscador de transacciones (Tipo de transacción: compra o venta)"])
        opcion_menu = input("  Elija una opción: ")
        sub_menu = ["1. Buscar por ID de cliente", "2. Buscar por ID de vehículo", "3. Buscar por Rango de fechas"]
        self.tablas("{:<48}", sub_menu, ["Buscador de transacciones (ID de cliente, vehículo o rango de fechas)"])
        opcion_sub_menu = input("  Elija una opción: ")
        if opcion_menu in ["1", "2"]:
            if opcion_menu == "1":
                tipo_transaccion = self.transaccionesDb.buscarRegistrosPorParametro("Compra", "tipo_transaccion")
            else:
                tipo_transaccion = self.transaccionesDb.buscarRegistrosPorParametro("Venta", "tipo_transaccion")
            if opcion_sub_menu in ["1", "2", "3"]:
               cabecera = ["ID Transacción", "ID Vehículo", "ID Cliente", "Transacción", "Fecha", "Monto", "Observaciones"]
               if opcion_sub_menu == "1":
                   buscar = int(input("  Ingrese el ID del cliente: "))
                   resultados = self.buscarEnMemoriaPorParametro(buscar,tipo_transaccion, "id_cliente") 
                   cabecera = ["ID Transacción", "ID Vehículo", "ID Cliente", "Transacción", "Fecha", "Monto", "Observaciones"]
                   self.tablas_diccionario (cabecera, resultados, "ID Cliente", self.gestionarTransacciones, "el SubMenú de Transacciones")
               elif opcion_sub_menu == "2":
                   buscar = int(input("  Ingrese el ID del vehículo: "))
                   resultados = self.buscarEnMemoriaPorParametro(buscar,tipo_transaccion, "id_vehiculo")
                   self.tablas_diccionario (cabecera, resultados, "ID Vehículo", self.gestionarTransacciones, "el SubMenú de Transacciones") 
               elif opcion_sub_menu == "3":
                   fecha_desde = input("  Ingrese la fecha desde (YYYY-MM-DD): ")
                   fecha_hasta = input("  Ingrese la fecha hasta (YYYY-MM-DD): ")
                   self.validarFechas(fecha_desde, self.buscadorTransacciones)
                   self.validarFechas(fecha_hasta, self.buscadorTransacciones)
                   coleccion = []
                   for registro in tipo_transaccion:
                        if fecha_desde <= registro.get("fecha") <= fecha_hasta:
                           coleccion.append(registro)
                   resultados = coleccion
                   self.tablas_diccionario (cabecera, resultados, "Fecha", self.gestionarTransacciones, "el SubMenú de Transacciones")     
#################################
#################################
if __name__ == "__main__":     ##
    interface = InterfazConcesionario()
    interface.mainMenu()       ##
#################################
#################################
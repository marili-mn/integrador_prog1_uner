# Opción 1: Sistema de Gestión de Concesionaria de Vehículos Usados

## Objetivo
Desarrollar una solución de software para gestionar la compra, venta y mantenimiento de vehículos usados en una concesionaria.

Realizado el análisis de requerimientos con el gerente de la concesionaria se ha determinado necesario registrar los siguientes datos:

## Requerimientos

1. **Registro de Vehículos:**
    - ID de vehículo (número único y autoincremental)
    - Nº de Patente o Dominio
    - Marca
    - Modelo
    - Tipo (Sedán, Hatchback, SUV, Pick Up, etc)
    - Año
    - Kilometraje
    - Precio de Compra
    - Precio de Venta
    - Estado (Disponible, Reservado, Vendido)

2. **Gestión de Clientes:**
    - ID de Cliente (número único y autoincremental)
    - Nombre
    - Documento
    - Apellido
    - Dirección
    - Teléfono
    - Correo Electrónico

3. **Registro de Transacciones:**
    - ID de Transacción (número único y autoincremental)
    - ID de Vehículo
    - ID de Cliente
    - Tipo de Transacción (Compra/Venta)
    - Fecha
    - Monto
    - Observaciones

## Características del Software

- **Almacenamiento de Información:** utilización de archivos JSON para almacenar los datos solicitados.
- **Interfaces de usuario interactivas que permitan registrar:**
  - **Vehículos:**
    - Crear, editar y eliminar vehículos.
    - Listados de búsqueda por patente, marca, modelo y precios de compra/venta.
  - **Clientes:**
    - Crear, editar y eliminar clientes.
    - Listados de búsqueda por documento, por apellido y/o nombres.
  - **Transacciones:**
    - Registrar compras y ventas de vehículos.
    - Imprimir listados de compras por cliente, vehículo y rango de fechas (deben incluir totalizadores de montos de dinero).
    - Imprimir listados de ventas por cliente, vehículo y rango de fechas (deben incluir totalizadores de montos de dinero).

- **Funcionalidad Extra:**
  - Se deberá desarrollar una funcionalidad extra del software a criterio del alumno/grupo. Esta nueva funcionalidad puede incluir, como por ejemplo: desarrollo de interfaz gráfica, consumo de una API externa, búsquedas avanzadas, nuevas funcionalidades similares a las anteriores que aporten valor agregado, etc.


  ####
  vehiculos:
   buscamos ademas de loq  pide por estado ""okey""
  FALTA!!!!!    poner las funciones a los input del buscador xcej capitalize ""AL FNAL"
  ####
  Clientes:
  *******************buscar por DOCUMENTO x NOMBRE o por APELLIDO
  ####
  Transacciones:
  imprir compras y ventas x:
  cliente
  vehiculos
----  rango de fechas ---->
------  con totalizador de monto de dinero
  ####
from interface import InterfazConcesionario
#   Importa la clase InterfazConcesionario desde el modulo Interface
def main():
    interface = InterfazConcesionario()
    interface.mainMenu()
    #   llama al método mainMenu de la interface que trajimos dede el import

if __name__ == "__main__":
    main()
#   Este modulo evita que el módulo interface se ejecute si es importado como parte de otro programa
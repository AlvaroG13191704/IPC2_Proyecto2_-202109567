# Imports
import os

from f_menu.f_menu import first_menu


# Class menu
class Main_Menu:
    # constructor
    def __init__(self) -> None:
        pass

    def init_menu(self):
        option = 0

        while option != 4:
            print('Bienvenidos al servidor de Soluciones Guatemala SA')
            print('---------------------------------------------------')
            print("""
        ¿Qué desea hacer?
        1. Configuración de empresa
        2. Selecionar una empresa
        3. Manejo de puntos de atención 
        4. Salir
            """)
            option = int(input('Ingrese una opción: '))
            if option == 1: 
                os.system('cls')
                menu_1 = first_menu() # call the first menu
                menu_1.init_menu()
            elif option == 2:
                os.system('cls')
                print('Opción 2')
            elif option == 3:
                os.system('cls')
                print('Opción 3')
            elif option == 4:
                os.system('cls')
                print('ADIOS!')
            else:
                print('Ingrese una opción valida')
                os.system('cls')


# start our app
if __name__=="__main__":
    menu=Main_Menu()
    menu.init_menu()
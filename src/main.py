# Imports
import os

from f_menu.f_menu import first_menu
from s_menu.s_menu import second_menu
from t_menu.t_menu import third_menu
from tdas.linkedList import LinkedList


# Class menu
class Main_Menu:
    # constructor
    def __init__(self) -> None:
        self.companies = LinkedList()
        self.init_state = None
        self.selected = None

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
                a , b = menu_1.get_attibutes()
                if a.size != 0:                        
                    for i in range(a.size):
                        company = a.get_node(i)
                        self.companies.append(company)
                self.init_state = b

            elif option == 2:
                os.system('cls')
                menu_2 = second_menu(self.companies)
                menu_2.init_menu()
                selected = menu_2.get_selected()
                self.selected = selected
            elif option == 3:
                os.system('cls')
                menu_3 = third_menu(self.companies,self.init_state)
                #menu_3.prepare_all()
                menu_3.ini_menu()
            elif option == 4:
                os.system('cls')
                print('ADIOS!')
            else:
                print('Ingrese una opción valida')
                os.system('cls')


# start our app
if __name__ == "__main__":
    menu = Main_Menu()
    menu.init_menu()

# Imports
import os

from f_menu.f_menu import first_menu
from s_menu.s_menu import second_menu
from tdas.linkedList import LinkedList


# Class menu
class Main_Menu:
    # constructor
    def __init__(self) -> None:
        self.companies = LinkedList()
        self.init_states = LinkedList()

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
                if a.size == 0 or b.size == 0:                        
                    for i in range(a.size):
                        company = a.get_node(i)
                        self.companies.append(company)
                    
                    for i in range(b.size):
                        init = a.get_node(i)
                        self.init_states.append(init)
                
            elif option == 2:
                os.system('cls')
                menu_2 = second_menu(self.companies)
                menu_2.init_menu()
                selected = menu_2.get_selected()
                
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
if __name__ == "__main__":
    menu = Main_Menu()
    menu.init_menu()

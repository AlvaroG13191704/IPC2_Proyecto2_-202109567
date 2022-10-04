# imports 
import os
from classes.attention_point import attention_point_class
from classes.company import company_class
from classes.desk import desk_class
from classes.transaction import transaction_class
from f_menu.components.company_init_xml import company_init_xml
from f_menu.components.company_xml import company_xml
from tdas.linkedList import LinkedList

# first submenu
class first_menu:
    def __init__(self) -> None:
        self.linkedList_company = LinkedList()
        self.init_state = None

    def init_menu(self):
        option = 0
        while option != 5:
            print('\n \n')
            print('---------------------------------------------------')
            print('CONFIGURACIÓN DE EMPRESA')
            print('---------------------------------------------------')
            print("""
        ¿Qué desea hacer?
        1. Limpiar el sistema
        2. Cargar archivo de configuración
        3. Crear una nueva empresa
        4. Cargar archivo de configuración inicial para la prueba? 
        5. Regresar 
            """)
            option = int(input('Ingrese una opción: '))
            if option == 1: 
                os.system('cls')
                self.clean_data()
                print('Se ha limpiado el sistema')
            elif option == 2: # upload an xml file,read and return an object
                os.system('cls')
                self.company_config_file()
                print('Se ha cargado correctamente el archivo!')
            elif option == 3:
                os.system('cls')
                self.create_new_company()
                print('Se ha agregado la empresa correctamente!')
                print(self.linkedList_company.size)
            elif option == 4:
                os.system('cls')
                self.company_init_config_file()
                print('Se ha cargado correctamente el archivo!')
            elif option == 5:
                os.system('cls')
            else:
                print('Ingrese una opción valida')
                os.system('cls')

    def get_attibutes(self):
        return self.linkedList_company, self.init_state
        
    # fun to clean the data
    def clean_data(self):
        void = LinkedList()
        self.linkedList_company = void
        self.init_state = None
    
    # uploadFile of company config
    def company_config_file(self):
        route = input('Ingrese la dirección del archivo de la empresa: \n')
        company_list =  company_xml(route)
        for i in range(company_list.size):
            company = company_list.get_node(i)
            self.linkedList_company.append(company)
        os.system('cls')

    # def create a new company
    def create_new_company(self):
        option = 0
        print('Cree una nueva empresa')
        print('------------------------')
        # creating the id 
        id_company = int(input('Ingrese el id de la empresa: '))
        name = input('Ingrese el nombre de la emrpesa: ')
        abbre = input('Ingrese la abreviación de la empresa: ')
        print('-------------------------------------------------')
        # attention points
        attention_points_list = LinkedList()
        op = int(input('¿Cuántos puntos de atención poseé?: '))
        for i in range(op):
            print(f'Punto de atención No.{i+1}')
            id_point = int(input('Ingrese el id del punto de atención: '))
            name_point = input('Ingrese el nombre del punto de atención: ')
            direction_point = input('Ingrese la dirección del punto de atención: ')

            print('-------------------------------------------------')
            # ask for how much desks are 
            desks_list = LinkedList()
            op_desk = int(input('¿Cuántos escritorios poseé posee?: '))
            for j in range(op_desk):
                print(f'Escritorio No.{j+1}')
                id_desk = int(input('Ingrese el id del escritorio: '))
                identification_desk = input('Ingrese la identificación del escritorio: ')
                manager_desk = input('Ingrese el encargado del escritorio: ')
                # save and object desk
                desk = desk_class(id_desk,identification_desk,manager_desk)
                desks_list.append(desk)
            
            # add to the attention point
            point = attention_point_class(id_point,name_point,direction_point,desks_list)
            attention_points_list.append(point)
            
            # save an object attention point
        print('-------------------------------------------------')
        # transaction list
        trans_list = LinkedList()
        op_trans = int(input('¿Cuántas transacciones poseé? '))
        for i in range(op_trans):
            print(f'Transacción No.{i+1}')
            id_trans = int(input('Ingrese el id de la transacción: '))
            trans_name = input('Ingrese el nombre de la transacción: ')
            trans_time = int(input('Ingrese el tiempo de la transacción: '))

            # create and save an transaction object 
            trans = transaction_class(id_trans,trans_name,trans_time)
            trans_list.append(trans)
        
        #create an company object
        company = company_class(id_company,name,abbre,attention_points_list,trans_list)
        # add to global 
        self.linkedList_company.append(company)
        # ask again
        while option != 2:
            print('''
        1. Si
        2. No
            ''')
            option = int(input('¿Deseas crear otra empresa? '))

            if option == 1:
                os.system('cls')
                self.create_new_company()
            elif option == 2:
                os.system('cls')

    # upload the initial state
    def company_init_config_file(self):
        route = input('Ingrese la dirección del archivo de prueba : \n')
        init_state=company_init_xml(route)
        for i in range(init_state.size):
            init_single_state = init_state.get_node(i)
            self.init_state = init_single_state
        os.system('cls')



        







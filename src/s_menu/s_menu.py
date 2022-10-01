import os

class second_menu:

    def __init__(self,companies) -> None:
        self.companies = companies
        self.selected = None
    

    def get_selected(self):
        return self.selected
        
    def init_menu(self):
        option = 0
        option_p = 0
        print('--------------------------')
        print('LISTA DE EMPRESAS')
        print('--------------------------')

        for i in range(self.companies.size):
            company = self.companies.get_node(i)
            print(f'''
    No. {i + 1}
    {company.print_company()}
    ''')
        
        option = int(input('\nQué empresa desea realizar la prueba? \n'))
        os.system('cls')


        selected = self.companies.get_node(option-1)
        self.selected = selected

        print(f'''
    Se he seleccionado la empresa: {selected.name}
        ''')
        for i in range(selected.attentions_point.size):
            point = selected.attentions_point.get_node(i)
            print(f'''
    Punto de atención No. {i+1}
    {point.print_point()}
            ''')
        
        option_p = int(input('\nQué punto de atención desea utilizar? \n'))
        selected_p = selected.attentions_point.get_node(option_p-1)
        os.system('cls')


        print(f'''
    Se ha seleccionado la empresa: {selected.name}
    En el punto de atención: {selected_p.name}
        ''')
        # ask again
        ask = 0
        while ask != 2:
            print('''
        1. Si
        2. No
            ''')
            ask = int(input('¿Desea escoger nuevamente?'))

            if ask == 1:
                os.system('cls')
                self.init_menu()
            elif ask == 2:
                os.system('cls')

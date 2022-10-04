


import os
from tdas.linkedList import LinkedList


class third_menu:

    def __init__(self,companies,init_state) -> None:
        self.companies = companies
        self.init_state = init_state
        self.active_desk = None
        self.clients_queue = None
        self.company = None
        self.total_time = 0
        self.times = 0

    def ini_menu(self):
        print('  Estado inicial  ')
        print('---------------------')
        self.print_queue()
        self.print_grahpviz()
        self.times += 1
        option = 0
        while option != 2:
            print('''
    ---------------------------------
    1. Si
    2. No
    ---------------------------------
            ''')
            option = int(input('¿Deseas iniciar la prueba?\n'))
            if option == 1:
                os.system('cls')
                print('--------------------')
                print('  INICIANDO PRUEBA  ')
                print('---------------------')
                # iter throught void desks and asig them the clients, clean clients queue
                while self.clients_queue.size != 0:
                    
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is None:
                            client_queue = self.clients_queue.get_first()
                            desk.client = client_queue.name
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                    # get off the client
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is not None:
                            desk.client = None
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                    if self.clients_queue.size < self.active_desk.size:
                        for i in range(self.clients_queue.size):
                            desk = self.active_desk.get_node(i)
                            if desk.client is None:
                                client_queue = self.clients_queue.get_first()
                                desk.client = client_queue.name
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                    # get off the client
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is not None:
                            desk.client = None
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                print('Imprimir resultados ')
                    
            elif option == 2:
                os.system('cls')




    def prepare_all(self):
        active_desk = LinkedList()
        clients_queue = LinkedList()
        time = 0
        total_time = 0
        for i in range(self.companies.size):
            company = self.companies.get_node(i)
            if company.id == self.init_state.idCompany:
                self.company = company
                for j in range(company.attentions_point.size):
                    point = company.attentions_point.get_node(j)
                    if point.id == self.init_state.idPoint:
                        for d in range(point.desk_list.size):
                            desk = point.desk_list.get_node(d)
                            active_desk_id = self.init_state.activeDeskList.get_node(d) 
                            if active_desk_id is not None:
                                if desk.id == active_desk_id.id:
                                    desk.active = True
                                    active_desk.append(desk)

        self.active_desk = active_desk

        for i in range(self.init_state.clientsList.size):
            client = self.init_state.clientsList.get_node(i)
            for j in range(client.transList.size):
                trans = client.transList.get_node(j)
                for t in range(self.company.transactions.size):
                    trans_company = self.company.transactions.get_node(t)
                    if trans.id == trans_company.id:
                        time += int(trans_company.time)*int(trans.amout)
            
            client.total_time = time
            total_time += client.total_time
            self.total_time = total_time
            time = 0
            clients_queue.append(client)
        
        self.clients_queue = clients_queue

    def print_queue(self):
        for i in range(self.active_desk.size):
            desk = self.active_desk.get_node(i)
            print(desk.print_desk())
        print(' Fila de clientes ')
        print(f'{self.total_time}')
        print('------------------')
        print(self.clients_queue.print_client_value())
        # for i in range(self.clients_queue.size):
        #     if self.clients_queue.get_node(i) is not None:
        #         client = self.clients_queue.get_node(i)
        #         print(f'''
        # Cliente No. {i+1}
        # {client.print_client()}
        #         ''')


    def print_grahpviz(self):
        grahp = '''
graph  grafi{
    rankdir=TB;
    labelloc="t";
    label="Nombre de empresa";
    node[
        shape="circle"
        fixedsize=true
        width=1.3
        height=1
    ];
    subgraph cluster_attention_point {
        node [style=filled shape="circle"];
        style="filled";
        color="chocolate1";
        label="Punto de atencion";
        '''
        desks = ''
        for i in range(self.active_desk.size):
            desk_obj = self.active_desk.get_node(i)
            desk = f'''
        subgraph cluster_{i+1}
            '''
            desk += '{'
            desk += f'''
        node [style=filled shape="circle"];
        style="filled";
        color="honeydew4";
        label="Escritorio {i+1}";
        E_{i}[label="{desk_obj.client}"];        
            '''
            desk += '}'
            desks += desk

        grahp += desks

        clients = '''
        subgraph cluster_row {
        node [style=filled shape="circle"];
        style="filled";
        color="gray";
        label="En espera";        
        '''
        if self.clients_queue.size != 0:
            clients += self.clients_queue.print_client_name()
            clients += '''
            }
            '''
        else:
            clients += '''
        C[label="No hay clientes" shape="square"]
            '''
            clients += '''
            }
            '''
        grahp += clients
        grahp += '''
    }
}
        '''
        #print(grahp)
        file = open(f'graphviz_{self.times}.dot','w')
        file.write(grahp)
        file.close()
        os.system(f'dot -Tpng graphviz_{self.times}.dot -o image_{self.times}_graphviz.png')




        
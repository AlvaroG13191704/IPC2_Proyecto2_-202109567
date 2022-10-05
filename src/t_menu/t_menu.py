


import os
from classes.client import client_Class
from classes.client_transaction import client_transaction_class
from tdas.linkedList import LinkedList


class third_menu:

    def __init__(self,companies,init_states) -> None:
        self.companies = companies
        self.init_state = None
        self.init_states = init_states
        self.active_desk = None
        self.clients_queue = None
        self.company = None
        self.total_time = 0
        self.times = 0
        self.point = None
        self.times_in_queue = []

    def ini_menu(self):
        for i in range(self.init_states.size):
            state = self.init_states.get_node(i)
            print(f'''
    Simulación No.{i+1}
    -------------------
    {state.id} - {state.idCompany} - {state.idPoint}
            ''')
        
        option_state = int(input('¿Qué simulación deseas realizar?\n'))
        self.init_state = self.init_states.get_node(option_state-1)
        os.system('cls')
        self.prepare_all()
        option = 0
        while option != 4:
            print('  ESTADO INICIAL  ')
            print('---------------------')
            self.print_queue()
            self.print_grahpviz()
            self.times += 1
            print('''
    ---------------------------------
    1. Iniciar Prueba
    2. Activar o desactivar escritorio
    3. Agregar un nuevo cliente a la cola
    4. No Iniciar prueba
    ---------------------------------
            ''')
            option = int(input('¿Qué desea hacer?\n'))
            if option == 1:
                os.system('cls')
                print('--------------------')
                print('  INICIANDO PRUEBA  ')
                print('---------------------')
                # iter throught void desks and asig them the clients, clean clients queue
                while self.clients_queue.size != 0:
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is None and desk.active == True:
                            client_queue = self.clients_queue.get_first()
                            desk.client = client_queue.name
                            desk.times.append(float(client_queue.total_time))
                            desk.clients_done += 1
                            self.times_in_queue[1:]
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                    # get off the client
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is not None and desk.active == True:
                            desk.client = None
                    self.times += 1

                    if self.clients_queue.size < self.active_desk.size:
                        c = 0
                        while self.clients_queue.size != 0:
                            desk = self.active_desk.get_node(c)
                            if desk.client is None and desk.active == True:
                                client_queue = self.clients_queue.get_first()
                                desk.client = client_queue.name
                                desk.times.append(float(client_queue.total_time))
                                desk.clients_done += 1
                                self.times_in_queue[1:]
                            c += 1
                    self.print_queue()
                    self.print_grahpviz()
                    self.times += 1

                    # get off the client
                    for i in range(self.active_desk.size):
                        desk = self.active_desk.get_node(i)
                        if desk.client is not None:
                            desk.client = None
                    self.times += 1


                self.print_services_time()
                
            
            elif option == 2:
                os.system('cls')
                for i in range(self.active_desk.size):
                    desk = self.active_desk.get_node(i)
                    print(f'''
    {desk.print_desk()}
                    ''')
                option = int(input('¿Qué escritorio deseas activar o desactivar?\n'))
                desk_selected = self.active_desk.get_node(option-1)
                if desk_selected.active:
                    desk_selected.active = False
                else:
                    desk_selected.active = True
                print(f'Se ha activado el escritorio No. {option}')
                os.system('cls')
            elif option == 3:
                os.system('cls')
                dpi = input('Ingrese su número de dpi: \n')
                name = input('Ingrese su nombre:\n')
                trans_option = int(input('¿Cuantas transacciones deseas realizar?\n'))
                trans_list = LinkedList()
                for i in range(trans_option):
                    for t in range(self.company.transactions.size):
                        trans_company = self.company.transactions.get_node(t)
                        print(f'Transacción No.{t+1} ---- {trans_company.id} -- {trans_company.name}  ')

                    o = int(input('¿Cual transacción desea realizar?\n'))
                    obj_trans = self.company.transactions.get_node(o-1)
                    amout = int(input('¿Cuantas veces deseas realizar la transacción?\n'))
                    trans_obj = client_transaction_class(obj_trans.id,amout)
                    trans_list.append(trans_obj)

                client = client_Class(dpi,name,trans_list)
                time = 0
                for j in range(client.transList.size):
                    trans = client.transList.get_node(j)
                    for t in range(self.company.transactions.size):
                        trans_company = self.company.transactions.get_node(t)
                        if trans.id == trans_company.id:
                            time += int(trans_company.time)*int(trans.amout)

                client.total_time = time    
                self.times_in_queue.append(float(client.total_time))
                self.clients_queue.append(client)
                os.system('cls')
            
            elif option == 4:
                os.system('cls')
                    
                    

            

    def prepare_all(self):
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
                        self.point = point
                        for d in range(point.desk_list.size):
                            desk = point.desk_list.get_node(d)
                            for a in range(self.init_state.activeDeskList.size):
                                active_desk_id = self.init_state.activeDeskList.get_node(a)
                                if active_desk_id is not None:
                                    if desk.id == active_desk_id.id:
                                        desk.active = True

        self.active_desk = self.point.desk_list

        for i in range(self.init_state.clientsList.size):
            client = self.init_state.clientsList.get_node(i)
            for j in range(client.transList.size):
                trans = client.transList.get_node(j)
                for t in range(self.company.transactions.size):
                    trans_company = self.company.transactions.get_node(t)
                    if trans.id == trans_company.id:
                        time += int(trans_company.time)*int(trans.amout)
                    
            
            client.total_time = time
            self.times_in_queue.append(float(client.total_time))
            total_time += client.total_time
            self.total_time = total_time
            time = 0
            clients_queue.append(client)
        
        self.clients_queue = clients_queue


    def print_services_time(self):
        for i in range(self.active_desk.size):
            desk = self.active_desk.get_node(i)
            if len(desk.times) != 0:
                min_time = min(desk.times)
                max_time = max(desk.times)
                average = round(sum(desk.times)/len(desk.times),2)
                print(f'''
    -----------------------------------------
    Tiempos de servicio del escritorio {i+1} - {desk.manager} - {desk.id}
    - Clientes atendidos: {desk.clients_done}
    - Tiempo minimo: {min_time} min
    - Tiempo máximo: {max_time} min
    - Tiempo promedio: {average} min
                ''') 
            else:
                print(f'''
    -----------------------------------------
    Tiempos de servicio del escritorio {i+1} - {desk.manager} - {desk.id}
    - Clientes atendidos: {desk.clients_done}
    - Tiempo minimo: 0 min
    - Tiempo máximo: 0 min
    - Tiempo promedio: 0 min
                ''')                 


    def print_queue(self):
        min_time = min(self.times_in_queue)
        max_time = max(self.times_in_queue)
        average = round((min_time+max_time)/2,2)
        active_desk = 0
        desactive_desk = 0
        for i in range(self.active_desk.size):
            desk = self.active_desk.get_node(i)
            if desk.active:
                active_desk += 1
            else:
                desactive_desk += 1
        
        for i in range(self.active_desk.size):
            desk = self.active_desk.get_node(i)
            print(desk.print_desk())
        print(' Fila de clientes ')
        print('------------------')
        print(self.clients_queue.print_client_value())
        print('------------------')
        if self.clients_queue.size != 0:
            print(f'''
    Tiempos de espera
    - Tiempo minimo: {min_time} min
    - Tiempo máximo: {max_time} min
    - Tiempo promedio: {average} min
    - Escritorios totales: {self.active_desk.size}
    - Escritorios activos: {active_desk}
    - Escritorios desactivados: {desactive_desk}
    - Clientes por atender: {self.clients_queue.size}
            ''')
        else:
            print(f'''
    Tiempos de espera
    - No hay clientes - No hay tiempo de espera
    - Escritorios totales: {self.active_desk.size}
    - Escritorios activos: {active_desk}
    - Escritorios desactivados: {desactive_desk}
    - Clientes por atender: {self.clients_queue.size}
            ''')


    def print_grahpviz(self):
        grahp = '''
graph  grafi{
    rankdir=TB;
    labelloc="t";
    '''
        grahp += f'''
    label="Empresa: {self.company.name}";
        '''
        grahp += '''
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
        '''
        grahp += f'''
        label="Punto de atención: {self.point.name}";
        '''
        desks = ''
        for i in range(self.active_desk.size):
            desk_obj = self.active_desk.get_node(i)
            if desk_obj.active:

                desk = f'''
        subgraph cluster_{i+1}
                '''
                desk += '{'
                desk += f'''
        node [style=filled shape="circle"];
        style="filled";
        color="honeydew";
        label="Escritorio {i+1}";
        E_{i}[label="{desk_obj.client}"];        
                '''
                desk += '}'
                desks += desk
            else:
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
        file = open(f'images\\graphviz_{self.times}.dot','w')
        file.write(grahp)
        file.close()
        os.system(f'dot -Tpng images\\graphviz_{self.times}.dot -o images\\image_{self.times}_graphviz.png')




        
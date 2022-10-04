import xml.etree.ElementTree as ET
from classes.client import client_Class
from classes.client_transaction import client_transaction_class
from classes.init_desk import init_desk_class
from classes.initial_state import initial_state_class

from tdas.linkedList import LinkedList


def company_init_xml(content):

    tree = ET.parse(content)
    initial_list = tree.getroot()
    init_state = LinkedList()
    # read the initial list
    for i in initial_list:
        # iterate throught the initial config
        for initial_config in i.iter('configInicial'):
            id_config = initial_config.get('id')
            id_company = initial_config.get('idEmpresa')
            id_point = initial_config.get('idPunto')

            # main config
            active_desk_linked = LinkedList()
            # active desks 
            for j in initial_config:
                # iterate throught active desk
                for active_desks in j.iter('escritoriosActivos'):
                    for activate_desk in active_desks.iter('escritorio'):
                        id_desk = activate_desk.get('idEscritorio')
                        # get the id desk
                        desk_active = init_desk_class(id_desk)
                        active_desk_linked.append(desk_active)

                # iterate throught clients list
                client_linkedList = LinkedList()
                for client_list in j.iter('listadoClientes'):
                    # throught client
                    for client in client_list.iter('cliente'):
                        dpi = client.get('dpi')
                        client_name = client.find('nombre').text
                        
                        # throught transactions list
                        client_trans_linkedList = LinkedList()
                        for trans_client_list in client.iter('listadoTransacciones'):
                            # trans
                            for trans in trans_client_list.iter('transaccion'):
                                id_client = trans.get('idTransaccion')
                                amount = trans.get('cantidad')
                                # create a trans obj
                                trans = client_transaction_class(id_client,amount)
                                client_trans_linkedList.append(trans)
                        
                        # client
                        client_obj = client_Class(dpi,client_name,client_trans_linkedList)
                        client_linkedList.append(client_obj)

            # add a init state
            init = initial_state_class(id_config,id_company,id_point,active_desk_linked,client_linkedList)
            init_state.append(init)
    # RETURN
    return init_state
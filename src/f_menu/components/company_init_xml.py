import xml.etree.ElementTree as ET


def company_init_xml(content):

    tree = ET.parse(content)
    initial_list = tree.getroot()
    # read the initial list
    for i in initial_list:
        # iterate throught the initial config
        for initial_config in i.iter('configInicial'):
            id_config = initial_config.get('id')
            id_company = initial_config.get('idEmpresa')
            id_point = initial_config.get('idPunto')

            # main config
            print(id_config,id_company,id_point)

            # active desks 
            for j in initial_config:
                # iterate throught active desk
                for active_desks in j.iter('escritoriosActivos'):
                    for activate_desk in active_desks.iter('escritorio'):
                        id_desk = activate_desk.get('idEscritorio')

                        # get the id desk
                        print(id_desk)

                # iterate throught clients list
                for client_list in j.iter('listadoClientes'):
                    # throught client
                    for client in client_list.iter('cliente'):
                        dpi = client.get('dpi')
                        client_name = client.find('nombre').text
                        
                        print(dpi,client_name)
                        # throught transactions list
                        for trans_client_list in client.iter('listadoTransacciones'):
                            # trans
                            for trans in trans_client_list.iter('transaccion'):
                                trans_client = trans.get('idTransaccion')
                                amount = trans.get('cantidad')

                                print(trans_client,amount)

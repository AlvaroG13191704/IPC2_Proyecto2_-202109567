import xml.etree.ElementTree as ET


tree = ET.parse('entrada_c_e.xml')

company_list = tree.getroot()


for company in company_list:
    # main attributes
    print('Atributos principales')
    id_company = company.get('id')
    name = company.find('nombre').text
    abbreviation = company.find('abreviatura').text
    
    print(id_company,name,abbreviation)

    # points of attentions atributes and lists
    print('Puntos de atención')
    for attention_points in company.iter('listaPuntosAtencion'):
        # attention point
        for attention_point in attention_points.iter('puntoAtencion'):
            id_attention = attention_point.get('id')
            name_attention = attention_point.find('nombre').text
            direction = attention_point.find('direccion').text
            print(id_attention,name_attention,direction)

            # desk lists
            print('Escritorios')
            for desk_list in attention_point.iter('listaEscritorios'):
                # desk
                for desk in desk_list.iter('escritorio'):
                    id_desk = desk.get('id')
                    identification_desk = desk.find('identificacion').text
                    duty_manager_desk = desk.find('encargado').text
                    
                    print(id_desk,identification_desk,duty_manager_desk)
    
    # now for transactions
    print('Lista de transacciones')
    for trans_list in company.iter('listaTransacciones'):
        for trans in trans_list.iter('transaccion'):
            id_trans = trans.get('id')
            name_trans = trans.find('nombre').text
            time_trans = trans.find('tiempoAtencion').text
            
            print(id_trans,name_trans,time_trans)



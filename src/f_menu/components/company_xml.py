#Imports
import xml.etree.ElementTree as ET
from tdas.linkedList import LinkedList
from classes.attention_point import attention_point_class
from classes.company import company_class
from classes.desk import desk_class
from classes.transaction import transaction_class

# create an object of each company, then return them
def company_xml(content):
    tree = ET.parse(content)
    company_list = tree.getroot()
    list_company = LinkedList()
    for company in company_list:
        # main attributes
        id_company = company.get('id')
        name = company.find('nombre').text
        abbreviation = company.find('abreviatura').text
        
        # create the a linkedList to save the attention points 
        attention_points_linkedList = LinkedList()
        # points of attentions atributes and lists
        for attention_points in company.iter('listaPuntosAtencion'):
            # attention point
            for attention_point in attention_points.iter('puntoAtencion'):
                id_attention = attention_point.get('id')
                name_attention = attention_point.find('nombre').text
                direction = attention_point.find('direccion').text

                # desk lists
                linkedList_desks = LinkedList()

                for desk_list in attention_point.iter('listaEscritorios'):
                    # desk
                    for desk in desk_list.iter('escritorio'):
                        id_desk = desk.get('id')
                        identification_desk = desk.find('identificacion').text
                        duty_manager_desk = desk.find('encargado').text
                        
                        # create an desk object
                        desk = desk_class(id_desk,identification_desk,duty_manager_desk)
                        # append to the linked list desk
                        linkedList_desks.append(desk)
                
                # create an attention point object
                attention_point_obj = attention_point_class(id_attention,name_attention,direction,linkedList_desks)
                # add the obj to the linked list
                attention_points_linkedList.append(attention_point_obj)
    
        # now for transactions
        trans_linkedList = LinkedList()
        for trans_list in company.iter('listaTransacciones'):
            for trans in trans_list.iter('transaccion'):
                id_trans = trans.get('id')
                name_trans = trans.find('nombre').text
                time_trans = trans.find('tiempoAtencion').text
                # create an trans obj
                trans_obj = transaction_class(id_trans,name_trans,time_trans)
                trans_linkedList.append(trans_obj)

        # create a company obj
        company_obj = company_class(id_company,name,abbreviation,attention_points_linkedList,trans_linkedList)
        list_company.append(company_obj)
    
    return list_company

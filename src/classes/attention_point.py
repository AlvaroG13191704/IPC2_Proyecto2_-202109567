

# class for attention points

class attention_point_class:

    def __init__(self,id,name,direction,desk_list) -> None:
        self.id = id
        self.name = name
        self.direction = direction
        self.desk_list = desk_list

    def print_point(self):
        return f'''
    Punto de atención: {self.name}
    Id: {self.id}
    Dirección: {self.direction}
    Escritorios disponibles: {self.desk_list.size}
        '''

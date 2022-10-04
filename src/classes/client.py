
class client_Class:
    
    def __init__(self,dpi,name,transList) -> None:
        self.dpi = dpi
        self.name = name
        self.transList = transList
        self.total_time = 0 # in minutes

    def print_client(self):
        return f'''
    |Nombre: {self.name} - dpi: {self.dpi} - No. de transacciones {self.transList.size}  - Tiempo: {self.total_time}min
        '''
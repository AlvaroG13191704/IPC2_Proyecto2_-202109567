

class desk_class:

    def __init__(self,id,identification,manager) -> None:
        self.id = id
        self.identification = identification
        self.manager = manager
        self.active = False
        self.client = None
        self.times = []
        self.clients_done = 0

    
    def print_desk(self):
        return f''''
     _____________________________________   
    | Escritorio -> {self.identification} 
    | Encargado -> {self.manager}         
    | Atendiendo a -> {self.client}     
    |{" Activo" if self.active else " Desactivado" }   
    |_____________________________________
    
        '''
        
        
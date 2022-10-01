


class company_class:

    def __init__(self,id,name,abbreviation,attentions_point,transactions) -> None:
        self.id = id
        self.name = name
        self.abbreviation = abbreviation
        self.attentions_point = attentions_point
        self.transactions = transactions



    def print_company(self):
        return f'''
    Empresa: {self.name}
    Abreviación: {self.abbreviation}
    --------------------------------
'''
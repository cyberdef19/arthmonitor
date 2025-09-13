from model.fields.base_lab_field import BaseLabField

'''
Показник ШОЕ (ESR) - неспецифічний але чутливий показник наявності запального процесу
'''

class ESRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="ESR", unit="мм/год", min_val=2.0, max_val=15.0, **kwargs)
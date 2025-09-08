from fields.base_lab_field import BaseLabField

'''
Клас поля нейтрофіли
'''

class NeuField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'NEU', unit="10^9/l", min_val=2.0, max_val=7.0, **kwargs)
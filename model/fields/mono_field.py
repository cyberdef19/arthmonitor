from model.fields.base_lab_field import BaseLabField

'''
Клас поля моноцити
'''

class MonoField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'MON', unit="10^9/l", min_val=0.12, max_val=1.2, **kwargs)
from fields.base_lab_field import BaseLabField

'''
Клас поля тромбоцити
'''

class PLTField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'PLT' ,unit="10^9/l", min_val=150, max_val=400, **kwargs)
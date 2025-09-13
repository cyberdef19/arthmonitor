from model.fields.base_lab_field import BaseLabField

'''
Тромбоцити (PLT) - важливий показник запальної активності.
Впливає на розрахунок PLR і може свідчити про загострення хвороби
'''

class PLTField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'PLT' ,unit="10^9/l", min_val=150, max_val=400, **kwargs)
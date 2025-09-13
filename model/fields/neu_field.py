from model.fields.base_lab_field import BaseLabField

'''
Абсолютний показник кількості нейтрофілів (NEU) - показник вродженої запальної
відповіді.
Використовується в розрахунку NLR 
'''

class NeuField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'NEU', unit="10^9/l", min_val=2.0, max_val=7.0, **kwargs)
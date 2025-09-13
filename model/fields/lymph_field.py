from base_lab_field import BaseLabField

'''
Абсолютний показник кількості лімфоцитів (LYM) - відображає активність адаптивного імунітету.
Важливий в розрахунку LMR, NLR, PLR 
'''

class LymphField(BaseLabField):
    def __init__(self, value, **kwargs ):
        super().__init__(value, symb = 'LYM', unit="10^9/l", min_val=0.8, max_val=4.0, **kwargs)
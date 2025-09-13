from model.fields.base_lab_field import BaseLabField

'''
Розрахунковий показник LMR - кількість лімфоцитів/кількість моноцитів - індикатор регуляторної
активності імунної системи. 
- Високе значення харакетрне для аутоімуннихї станів, зокрема Th1/Th17-залежних процесів
- Зниження показника може свідчити про системне запалення або інфекцію 
 
'''

class LMRField(BaseLabField):
    
    def __init__(self, value, **kwargs):
        super().__init__(value, symb = 'LMR', **kwargs)
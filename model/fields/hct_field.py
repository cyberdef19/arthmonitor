from model.fields.base_lab_field import BaseLabField

'''
Показник Гемтокрит (HCT) - свідчить про ступінь згущення крові, може бути важливим
при оцінці запалення
'''

class HCTField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb='HCT', unit='%', min_val=31.0, max_val=51.0, **kwargs )
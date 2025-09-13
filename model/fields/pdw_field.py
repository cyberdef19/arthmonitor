from model.fields.base_lab_field import BaseLabField

'''
Показник ширина розподілу тромбоцитів (PDW) - свідчить про активацію стрес тромбоцитів,
може бути ознакою хронічного запалення 
'''

class PDWField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="PDW", unit="fL", min_val=15.0, max_val=17.0, **kwargs)
from model.fields.base_lab_field import BaseLabField

'''
Розрахунковий показник PLR = кількість тромбоцитів/кількість лімфоцитів - непрямий маркер запального
процесу.
- Високе значення свідчить про активацію тромбоцитарноїланки на тлі хронічного запалення
- Може бути корисним для диференціації між аутоімунним і неаутомінним запаленням

'''

class PLRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="PLR", **kwargs)


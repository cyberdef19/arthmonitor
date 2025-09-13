from model.fields.base_lab_field import BaseLabField

'''
Показник швидкості зміни функції LMR за часом - похідна за часом.
'''

class DLMRdtField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="DLMRdt", **kwargs)
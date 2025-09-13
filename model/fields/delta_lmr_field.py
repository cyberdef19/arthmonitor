from model.fields.base_lab_field import BaseLabField

'''
Дельта LMR - Зміна LMR між поточним та попереднім значенням показника LMR
'''

class DeltaLMRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="DeltaLMR", **kwargs)
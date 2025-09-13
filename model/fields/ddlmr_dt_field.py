from model.fields.base_lab_field import BaseLabField

'''
Показник прискорення зміни функції LMR за часом -друга похідна за часом.
'''

class DDLMRdtField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="DDLMRdt", **kwargs)
from model.fields.base_lab_field import BaseLabField

'''
Інтегральний індекс реактивності за певний період.
'''

class IntegralLMRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="IntegralLMR", **kwargs)
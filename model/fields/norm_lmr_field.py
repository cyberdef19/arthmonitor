from model.fields.base_lab_field import BaseLabField

'''
Показник нормалізованого індекса LMR приведений до стандартної шкали(0-1).
'''

class NormLMRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="NormLMR", **kwargs)
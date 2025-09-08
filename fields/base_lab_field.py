from tortoise import fields
'''
Базовий клас для реалізації полів класів 
'''

class BaseLabField(fields.FloatField):

    def __init__(self,
                 real_val: any,
                 symb: str = "",
                 unit: str = "",
                 min_val: float = None,
                 max_val: float = None,
                 **kwargs):
        super().__init__(**kwargs)
        self.unit = unit
        self.symb = symb
        self.max_val = max_val
        self.min_val = min_val
        self.real_val = real_val
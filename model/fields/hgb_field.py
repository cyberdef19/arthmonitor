from model.fields.base_lab_field import BaseLabField

'''
Показник Гемоглобін (HGB) - може знижуватися при хронычному запаленні
 та анемії, впливаєна оцінку загального стану
'''

class HGBField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="HGB", unit="g/L", min_val=131.0,max_val=173.0, **kwargs)

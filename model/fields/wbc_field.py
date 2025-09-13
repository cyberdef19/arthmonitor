from model.fields.base_lab_field import BaseLabField

'''
Показник WBC - загальна кількість лейкоцитів - узагальнений показник запалення,
впливаєна NEU, LYM, MON 
'''

class WBCField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="WBC", unit="10^9/l", min_val=4.0, max_val=10.0, **kwargs)
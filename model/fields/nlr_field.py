from model.fields.base_lab_field import BaseLabField

'''
Розрахунковий показник NLR = кількість нейтрофілів/кількість лімфоцитів - запальний маркер системного
запалення.
-Підвищується при загостренні хронічного запалення, інфекціях або фізіологічному стресі
-Важливий для оцінки балансу вродженого та адаптивного імунітету
'''

class NLRField(BaseLabField):
    def __init__(self, value, **kwargs):
        super().__init__(value, symb="NLR", **kwargs)
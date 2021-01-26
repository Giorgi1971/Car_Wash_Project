from django.db.models import IntegerChoices


class TypeChoices(IntegerChoices):
    '''(
        (1, 'Male',),
        (2, 'Female',),
        (3, 'Other1',),
        )
    '''
    Sedan = 1
    Jip = 2
    Mini = 3

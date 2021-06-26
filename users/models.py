from django.db import models

class SortUser(models.Model):
    MAlE = 'MALE'
    FEMALE = 'FEMALE'

    GENDER = [(MAlE, 'male'), (FEMALE, 'female')]

    A1 = '1'
    A2 = '2'
    B1 = '3'
    B2 = '4'
    C1 = '5'

    ENGLISH_LEVEL = [(A1, 'A1'), (A2, 'A2'), (B1, 'B1'), (B2, 'B2'),
                     (C1, 'C1')]

    user_name = models.CharField(max_length=100, verbose_name='user level')
    gender = models.CharField(max_length=7, choices=GENDER, default=MAlE, verbose_name='gender')
    age = models.PositiveIntegerField(default=18)
    english_level = models.CharField(max_length=20, choices=ENGLISH_LEVEL, verbose_name='English level')

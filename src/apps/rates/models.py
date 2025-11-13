### https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-types < Referência para Criação dos tipos
from django.db import models
from config.settings.base import ALLOWED_CURRENCIES

class Rate (models.Model):

    date = models.DateField(null=False,blank=False)
    base = models.CharField(max_length=3,null=False,blank=False,default='USD')  
    currency = models.CharField(
        max_length=3,
        choices=[(c, c) for c in ALLOWED_CURRENCIES],
        unique=False,
        null=False,
        blank=False
    )
    value = models.DecimalField(null=True,blank=False,decimal_places= 2, max_digits=10)  

    def __str__(self):
        return f'{self.date} | {self.base} → {self.currency} = {self.value}'


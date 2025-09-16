### https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-types < Referência para Criação dos tipos
from django.db import models

class Rate (models.Model):

    date = models.DateField()
    base = models.CharField(max_length=3)  
    currency = models.CharField(max_length=3)  
    value = models.FloatField()  

    def __str__(self):
        return f'{self.date} | {self.base} → {self.currency} = {self.value}'


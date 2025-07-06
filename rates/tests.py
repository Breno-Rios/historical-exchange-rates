#https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Server-side/Django/Testing
from django.test import TestCase
from rates.models import Rate
from datetime import date

# Create your tests here.

class RateModelTest(TestCase):
  def test(self):
    self.Rate = Rate.objects.create(date= date(2025, 7, 5), base= 'USD', currency = 'BRL' ,value = 2.00)

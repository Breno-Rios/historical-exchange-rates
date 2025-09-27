from django.test import TestCase
from apps.rates.models import Rate
from datetime import date


class RateModelTest(TestCase):
  def teste_models_create_rate_is_ok(self):
    obj= Rate.objects.create(date= date(2025, 7, 5), base= 'USD', currency = 'BRL' ,value = 2.00)
    self.assertIsInstance(obj,Rate)
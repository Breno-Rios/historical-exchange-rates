from django.test import TestCase
from src.apps.rates import service


# Create your tests here.

class RateServicesTest(TestCase):
  def test_service_function_get_rates_by_not_is_error(self):
    rate = service.get_rates_by('2025-07-01','BRL')
    self.assertIsNot(rate, ValueError)
    
  def test_service_function_insert_rate_is_ok(self):
    obj = {
            "date": "2025-07-01",
            "base": "USD",
            "rates": {
                "BRL": 5.25
            }
        }
    service.insert_rate(obj)
    rate = service.get_rates_by('2025-07-01','BRL')
    value = rate.values('value').first()['value']
    self.assertEqual(value,5.25)

  def test_service_function_fetch_and_save_rates_return_is_list(self):
    lista= service.fetch_and_save_rates(['2025-07-01'], 'USD', 'BRL')
    self.assertIsInstance(lista, list)

  def test_service_function_validate_currencies_is_ok(self):
    service.validate_currencies('USD',"BRL")
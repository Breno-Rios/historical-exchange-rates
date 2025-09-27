from django.test import TestCase
from apps.rates import utils

class RatesUtilsTest(TestCase):
  def test_rates_generate_date_range_is_valid(self):
      start = '2025-07-01'
      end = '2025-07-05'
      list_date = utils.generate_date_range(start,end)
      self.assertIsInstance(list_date,list)

  def test_rates_is_valid_date_is_ok(self):
      start = '2025-07-01'
      day = utils.is_valid_date(start)
      assert day == True
      
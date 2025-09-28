from django.test import TestCase
from apps.api.utils.exchange_date_formater import DateFormatter
import pytest
class DateFormatValidator(TestCase):

  def test_should_always_return_date_iso_fmt(self):
      fmt1 = '2025-01-01'
      convert_fmt1 = DateFormatter.fromisoformat(fmt1)
      self.assertIsInstance(convert_fmt1, DateFormatter)
      print(convert_fmt1)

  def test_should_always_return_exception_if_input_is_invalid(self):
      fmt2 = '01/01/2025'
      with pytest.raises(ValueError):
        convert_fmt2 = DateFormatter.fromisoformat(fmt2)

from django.test import TestCase
from apps.api.validators.currency_code_validator import CurrencyValidator, ALLOWED_CURRENCIES
import pytest
class DateFormatValidator(TestCase):

  def test_should_return_code_exception(self):
    with pytest.raises(ValueError):
      code = CurrencyValidator.validate('brl')
  
  def test_should_input_code_is_equal_output_code(self):
    code = 'BRL'
    validate_code = CurrencyValidator.validate(code)
    self.assertEqual(code,validate_code)
from django.test import TestCase
from apps.api.serializers.exchange_rates_serializer import ExchangeRatesSerializer
from apps.rates.models import Rate
import datetime
from decimal import Decimal


class DateFormatValidator(TestCase):
    def test_should_returns_list_of_dicts(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data = list(Rate.objects.all())
        output = ExchangeRatesSerializer.list_to_dict(data)
        self.assertIsInstance(output, list)

    def test_should_coantains_all_keys_of_dict(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data = list(Rate.objects.all())
        output = ExchangeRatesSerializer.list_to_dict(data)
        expected_keys = {"id", "date", "base_code", "currency_code", "value"}
        self.assertEqual(set(output[0].keys()), expected_keys)

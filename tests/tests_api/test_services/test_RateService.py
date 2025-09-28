from django.test import TestCase
from apps.api.services.exchange_rates_services import RateService
from apps.rates.models import Rate

import datetime
from decimal import Decimal


class RateServicesTest(TestCase):

    def test_get_all_currency_exchange_rates_returns_list(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data = RateService.get_all_currency_exchange_rates()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)

    def test_get_currency_exchange_rates_by_date_returns_list(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data2 = RateService.get_currency_exchange_rates_by_date(
            date='2025-09-01')
        self.assertIsInstance(data2, list)
        self.assertEqual(len(data2), 1)

    def test_get_currency_exchange_rates_by_currency_returns_list(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data3 = RateService.get_currency_exchange_rates_by_currency(
            target_currency='BRL')
        self.assertIsInstance(data3, list)
        self.assertEqual(len(data3), 1)

    def test_get_currency_exchange_rates_by_data_range_returns_list(self):
        Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))

        data4 = RateService.get_currency_exchange_rates_by_data_range(
            start_date='2025-08-31', end_date='2025-09-02')
        self.assertIsInstance(data4, list)
        self.assertEqual(len(data4), 1)

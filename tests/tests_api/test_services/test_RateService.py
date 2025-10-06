from django.test import TestCase
from apps.api.services.exchange_rates_services import RateService
from apps.rates.models import Rate
from apps.utils.date_generator import DateGenerator

import datetime
from decimal import Decimal


class RateServicesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rate1 = Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))
        
        cls.rate2 = Rate.objects.create(id=2, date=datetime.date(
            2025, 9, 2), base="USD", currency="BRL", value=Decimal("5.4278"))
        
        cls.rate3 = Rate.objects.create(id=3, date=datetime.date(
            2025, 9, 3), base="USD", currency="BRL", value=Decimal("5.4278"))

    def test_get_all_currency_exchange_rates_returns_list(self):

        data = RateService.get_all_currency_exchange_rates()
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 3)

    def test_get_currency_exchange_rates_by_date_returns_list(self):

        data2 = RateService.get_currency_exchange_rates_by_date(
            date='2025-09-01')
        self.assertIsInstance(data2, list)
        self.assertEqual(len(data2), 1)

    def test_get_currency_exchange_rates_by_currency_returns_list(self):

        data3 = RateService.get_currency_exchange_rates_by_currency(
            target_currency='BRL')
        self.assertIsInstance(data3, list)
        self.assertEqual(len(data3), 3)

    def test_get_currency_exchange_rates_by_data_range_returns_list(self):

        data4 = RateService.get_currency_exchange_rates_by_data_range(
            start_date='2025-08-31', end_date='2025-09-02')
        self.assertIsInstance(data4, list)
        self.assertEqual(len(data4), 2)

    def test_should_returns_equal_exchange_rates_missing_dates_with_expected_output(self):
        
        start_date = datetime.date(2025, 9, 1) 
        end_date = datetime.date(2025, 9, 5)

        all_dates = DateGenerator.range_dates(start_date, end_date)

        existing_dates = Rate.objects.filter(
                date__range=(start_date, end_date),
                 base="USD",
                 currency="BRL"
                ).values_list("date", flat=True)

        missing_dates = [d for d in all_dates if d not in existing_dates]
        
        expected = [datetime.date(2025, 9, 4), datetime.date(2025, 9, 5)]

        self.assertEqual(missing_dates, expected)
    
    def test_get_dashboard_currency_exchange_rates(self):

        data5 =RateService.get_dashboard_currency_exchange_rates(start_date= datetime.date(2025, 9, 1), end_date = datetime.date(2025, 9, 5), base_currency='USD', target_currency= 'BRL')
        
        # self.assertIsInstance(data5, list)
        # self.assertEqual(len(data5), 5)
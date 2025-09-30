from django.test import TestCase
from django.test import TestCase
from apps.rates.models import Rate
from django.db.models.query import QuerySet
from apps.api.repository.rate_repository import RateRepository

import datetime
from decimal import Decimal


class RateRepositoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.rate1 = Rate.objects.create(id=1, date=datetime.date(
            2025, 9, 1), base="USD", currency="BRL", value=Decimal("5.4278"))
    
    def test_find_all_returns_queryset(self):
        data = RateRepository.find_all()
        self.assertIsInstance(data, QuerySet)

    def test_find_by_date_returns_queryset(self):
        data2 = RateRepository.find_by_date( date='2025-09-01')
        self.assertIsInstance(data2, QuerySet)


    def test_find_by_currency_returns_queryset(self):
        data3 = RateRepository.find_by_currency(target_currency='BRL')
        self.assertIsInstance(data3, QuerySet)

    def test_find_by_data_range_returns_queryset(self):
        data4 = RateRepository.find_by_data_range(
            start_date='2025-08-31', end_date='2025-09-02')
        self.assertIsInstance(data4, QuerySet)

    def test_find_by_data_range_and_filters_returns_queryset(self):
        data5 = RateRepository.find_by_data_range_and_filters(start_date='2025-08-31', end_date='2025-09-02', currency='BRL')
        self.assertIsInstance(data5, QuerySet)
     

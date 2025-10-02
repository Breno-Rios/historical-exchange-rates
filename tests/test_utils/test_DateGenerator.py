from django.test import TestCase
from apps.utils.date_generator import DateGenerator
import datetime 
import pytest

class DateGeneratorTest(TestCase):
    
    def test_should_returns_range_of_dates(self):
        start = datetime.date(2025,9,1)
        end = datetime.date(2025,9,10)
        date_list = DateGenerator.range_dates(start= start, end= end)
        self.assertIsInstance(date_list, list)
    def test_should_returns_range_of_iso_dates(self):
        start = datetime.date(2025,9,1)
        end = datetime.date(2025,9,10)
        date_list = DateGenerator.range_iso_dates(start= start, end= end)
        self.assertIsInstance(date_list, list)
    def test_should_return_exception_because_end_date_before_start_date(self):
        start = datetime.date(2025,9,10)
        end = datetime.date(2025,9,1)
        with pytest.raises(ValueError):
            DateGenerator.range_iso_dates(start= start, end= end)

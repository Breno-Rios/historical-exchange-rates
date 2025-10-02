from django.test import TestCase
import datetime
import pytest

from apps.utils.date_generator import DateGenerator
from apps.utils.workday import filter_only_five_workdays

class workdays(TestCase):

    def test_not_is_workday(self):
        start = datetime.date(2025,9,6).isoweekday()
        self.assertEqual(start,6)

    def test_should_return_only_3_workdays(self):
        start = datetime.date(2025,9,6)
        end = datetime.date(2025,9,10)
        dates_list = DateGenerator.range_dates(start, end)

        workdays = filter_only_five_workdays(dates_list)

        self.assertEqual(len(workdays), 3)

    def test_return_exception_because_period_is_greater_than_5_workdays(self):
        start = datetime.date(2025,9,8)
        end = datetime.date(2025,9,13)
        dates_list = DateGenerator.range_dates(start, end)

        with pytest.raises(ValueError):
             filter_only_five_workdays(dates_list)
    
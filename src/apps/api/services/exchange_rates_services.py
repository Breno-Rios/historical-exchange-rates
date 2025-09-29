from apps.rates.models import Rate
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist


class RateService:

    @staticmethod
    def get_all_currency_exchange_rates():
        try:
            rates_list = list(Rate.objects.all())
            return rates_list
        except ObjectDoesNotExist as e:
            raise (f'error: {e}')

    @staticmethod
    def get_currency_exchange_rates_by_date(date: datetime):
        try:
            rates_list = list(Rate.objects.filter(date=date))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(
                f'error: {e}, No rates found for date {date}')

    @staticmethod
    def get_currency_exchange_rates_by_currency(target_currency: str):
        try:
            rates_list = list(Rate.objects.filter(
                currency=target_currency))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(
                f'error: {e}, No rates found for currency {target_currency}')

    @staticmethod
    def get_currency_exchange_rates_by_data_range(start_date: datetime, end_date: datetime):
        try:
            rates_list = list(Rate.objects.filter(
                date__range=(start_date, end_date)))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist('error: {e}, No rates found in period')

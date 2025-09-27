from apps.rates.models import Rate
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

class RateService:

    @staticmethod
    def get_all_currency_exchange_rates():
        try:
            list_rates = list(Rate.objects.all().values_list())
            return list_rates
        except ObjectDoesNotExist as e:
            raise (f'error: {e}')
                  
    @staticmethod
    def get_currency_exchange_rates_by_date(date: datetime):
        try:
            list_rates = list(Rate.objects.filter(date = date).values_list())
            return list_rates
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(f'error: {e}, No rates found for date {date}')
        
    
    @staticmethod
    def get_currency_exchange_rates_by_currency(target_currency: str):
        try:
            list_rates = list(Rate.objects.filter(currency = target_currency).values_list())
            return list_rates
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(f'error: {e}, No rates found for currency {target_currency}')
    
    @staticmethod
    def get_currency_exchange_rates_by_data_range(start_date: datetime, end_date: datetime):
        try:
            list_rates = list(Rate.objects.filter(date__range=(start_date, end_date)).values_list())
            return list_rates
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist('error: {e}, No rates found in period')


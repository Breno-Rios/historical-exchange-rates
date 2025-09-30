from apps.rates.models import Rate
from datetime import datetime

class RateRepository:

    @staticmethod
    def find_all():
        return Rate.objects.all()

    @staticmethod
    def find_by_date(date: datetime):
        return Rate.objects.filter(date=date)

    @staticmethod
    def find_by_currency(target_currency: str):
        return Rate.objects.filter(currency= target_currency)

    @staticmethod
    def find_by_data_range(start_date: datetime, end_date: datetime):
        return Rate.objects.filter( date__range=(start_date, end_date))
    
    @staticmethod
    def insert(date, base, currency, value):
        Rate.objects.create(
                date=date,
                base=base,
                currency=currency,
                value=value
            )




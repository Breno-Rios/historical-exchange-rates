from apps.rates.models import Rate
from datetime import datetime

class RateRepository:

    def find_all(self, ):
        return Rate.objects.all()

    def find_by_date(self, date: datetime):
        return Rate.objects.filter(date=date)

    def find_by_currency(self, target_currency: str):
        return Rate.objects.filter(currency= target_currency)

    def find_by_data_range(self, start_date: datetime, end_date: datetime):
        return Rate.objects.filter( date__range=(start_date, end_date))
    
    def find_by_data_range_and_filters(self, start_date: datetime, end_date: datetime,**filters):
        return Rate.objects.filter(
                    date__range=(start_date, end_date),
                    **filters  
                ).order_by('date')
    
    def insert(self, date, base, currency, value):
        Rate.objects.update_or_create(
                date=date,
                base=base,
                currency=currency,
                value=value
            )




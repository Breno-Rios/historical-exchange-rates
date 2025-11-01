from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from apps.api.repository.rate_repository import RateRepository
from apps.utils.date_generator import DateGenerator
from apps.utils.workday import filter_only_five_workdays
from apps.api.clients.api_vatcomply import ClientVatcomply
from apps.rates.models import Rate
from datetime import date
from decimal import Decimal

class RateService:
    def __init__(self, repository: RateRepository):
        self.repository: RateRepository = repository

    def __insert_external_obj_exchange_rates(self, dates: list, base_currency:str, target_currency: str):
        
        client =  ClientVatcomply.fetch_by_dates(base_currency,target_currency,dates)

        for data in client:
            self.repository.insert(
                date=data['date'],
                base=data['base'],
                currency=list(data['rates'].keys())[0],
                value=list(data['rates'].values())[0]
            )

    def get_dashboard_currency_exchange_rates(self, start_date: datetime, end_date: datetime, base_currency:str, target_currency: str):
        try:
            
            all_dates = filter_only_five_workdays(DateGenerator.range_dates(start_date, end_date))

            filters = dict(start_date = start_date, end_date= end_date, base = base_currency, currency = target_currency)

            rates_queryset = self.find_by_data_range_and_filters(**filters)

            existing_dates = rates_queryset.values_list("date", flat=True)
            missing_dates = [d for d in all_dates if d not in existing_dates]

            if not missing_dates:
                return rates_queryset
            
            self.__insert_external_obj_exchange_rates(missing_dates, base_currency, target_currency)
            
            return self.find_by_data_range_and_filters(**filters)
                           
    
        except ObjectDoesNotExist as e:
            raise (f'error: {e}')


    def find_all(self):
        try:
            queryset = self.repository.find_all()
            return queryset
        except queryset.ObjectDoesNotExist as e:
            raise (f'error: {e}')
        
    def find_by(self, **filters):
       try:
           queryset = self.repository.find_by(**filters) 
           return queryset
       except queryset.ObjectDoesNotExist as e:
            raise (f'error: {e}')
        
    def find_by_data_range_and_filters(self, **filters):
        try:
           start = filters.pop('start_date')
           end = filters.pop('end_date')
           queryset = self.repository.find_by_data_range_and_filters(start_date=start, end_date=end, **filters) 
           return queryset
        except queryset.ObjectDoesNotExist as e:
            raise (f'error: {e}')
        
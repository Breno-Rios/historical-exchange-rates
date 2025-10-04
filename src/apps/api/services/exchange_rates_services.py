from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from apps.api.repository.rate_repository import RateRepository
from apps.utils.date_generator import DateGenerator
from apps.utils.workday import filter_only_five_workdays
from apps.api.external_api import api_vatcomply_com_rates


class RateService:

    @staticmethod
    def __insert_external_obj_exchange_rates(dates: list, base_currency:str, target_currency: str):

        for date in dates:

            params={
                "base": base_currency,
                "symbols": target_currency,
                "date": date
            }
            response = api_vatcomply_com_rates.get_vatcomply_exchange_rates(params=params)
            data = response.json()

            currency = list(data.get('rates'))[0]
            RateRepository.insert(date= data.get('date'),
                                  base=data.get('base'),
                                  currency=currency,
                                  value=data.get('rates').get(currency)
                                  )

    @staticmethod
    def get_dashboard_currency_exchange_rates(start_date: datetime, end_date: datetime, base_currency:str, target_currency: str):
        try:

            if base_currency == None:
                base_currency = 'USD'

            all_dates = filter_only_five_workdays(DateGenerator.range_dates(start_date, end_date))

            rates_queryset = RateRepository.find_by_data_range_and_filters(
                start_date,
                end_date,
                base= base_currency,
                currency= target_currency
            )

            existing_dates = rates_queryset.values_list("date", flat=True)
            missing_dates = [d for d in all_dates if d not in existing_dates]

            if not missing_dates:
                return list(rates_queryset)
            
            RateService.__insert_external_obj_exchange_rates(missing_dates, base_currency, target_currency)

            return list(
                        RateRepository.find_by_data_range_and_filters(
                            start_date,
                            end_date,
                            base= base_currency,
                            currency= target_currency
                            )
                        )
    
        except ObjectDoesNotExist as e:
            raise (f'error: {e}')


    @staticmethod
    def get_all_currency_exchange_rates():
        try:
            rates_list = list(RateRepository.find_all())
            return rates_list
        except ObjectDoesNotExist as e:
            raise (f'error: {e}')

    @staticmethod
    def get_currency_exchange_rates_by_date(date: datetime):
        try:
            rates_list = list(RateRepository.find_by_date(date=date))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(
                f'error: {e}, No rates found for date {date}')

    @staticmethod
    def get_currency_exchange_rates_by_currency(target_currency: str):
        try:
            rates_list = list(RateRepository.find_by_currency(target_currency=target_currency))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist(
                f'error: {e}, No rates found for currency {target_currency}')

    @staticmethod
    def get_currency_exchange_rates_by_data_range(start_date: datetime, end_date: datetime):
        try:
            rates_list = list(RateRepository.find_by_data_range(start_date, end_date))
            return rates_list
        except ObjectDoesNotExist as e:
            raise ObjectDoesNotExist('error: {e}, No rates found in period')
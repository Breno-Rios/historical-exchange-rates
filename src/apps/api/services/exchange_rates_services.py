from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from apps.api.repositories.rate_repository import RateRepository
from apps.utils.workday import Workdays
from apps.api.clients.api_vatcomply import ClientVatcomply
from apps.rates.models import Rate
from datetime import date
from decimal import Decimal


class RateAPIService:
    def __init__(self, repository: RateRepository):
        self.repository: RateRepository = repository

    def find_all(self):
        try:
            queryset = self.repository.find_all()
            return queryset
        except ObjectDoesNotExist as e:
            raise ValueError(f'error: {e}')

    def find_by(self, **filters):
        try:
            queryset = self.repository.find_by(**filters)
            return queryset
        except ObjectDoesNotExist as e:
            raise ValueError(f'error: {e}')

    def find_by_data_range_and_filters(self, **filters):
        try:
            start = filters.pop('start_date')
            end = filters.pop('end_date')

            validator = Workdays(
                start, end).filtered_period_is_valid(max_days=5)

            if not validator:
                raise ValueError(
                    "Error: the period must not exceed 5 workdays")

            queryset = self.repository.find_by_data_range_and_filters(
                start_date=start, end_date=end, **filters)
            return queryset
        except ObjectDoesNotExist as e:
            raise ValueError(f'error: {e}')


class RateDashboardService:

    def __init__(self, repository: RateRepository, rate_api: RateAPIService):
        self.repository: RateRepository = repository
        self.rate_api: RateAPIService = rate_api

    def _get_missing_dates(self, workdays_period, **filters):

        rates_queryset = self.rate_api.find_by_data_range_and_filters(**filters)
        existing_dates = rates_queryset.values_list("date", flat=True)
        missing_dates = [d for d in workdays_period if d not in existing_dates]
        return missing_dates

    def _save_new_rates(self, client_data):
        for data in client_data:
            self.repository.insert(
                date=data['date'],
                base=data['base'],
                currency=list(data['rates'].keys())[0],
                value=list(data['rates'].values())[0]
            )

    def get_dashboard_currency_exchange_rates(self, start_date: datetime, end_date: datetime, base: str, currency: str):

        try:
            workdays = Workdays(start_date, end_date)

            if not workdays.filtered_period_is_valid(max_days=5):
                raise ValueError("Error: the period must not exceed 5 workdays")

            workdays_period = workdays.generate_workdays()

            filters = dict(start_date=start_date, end_date=end_date,
                            base=base, currency=currency)

            missing_dates = self._get_missing_dates(workdays_period, **filters)

            if missing_dates:
                client = ClientVatcomply.fetch_by_dates(
                    base, currency, missing_dates)

                self._save_new_rates(client)

            return self.rate_api.find_by_data_range_and_filters(**filters)

        except ObjectDoesNotExist as e:
            raise ValueError(f'error: {e}')


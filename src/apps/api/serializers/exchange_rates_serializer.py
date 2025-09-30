from apps.rates.models import Rate
from apps.utils.exchange_date_formater import DateFormatter


class ExchangeRatesSerializer():

    @staticmethod
    def to_dict(instance) -> dict:
        data = {
            'id': instance.id,
            'date': DateFormatter.isoformat(instance.date),
            'base_code': instance.base,
            'currency_code': instance.currency,
            'value': str(instance.value)
        }
        return data

    @classmethod
    def list_to_dict(cls, list_of_queryset):
        return [cls.to_dict(obj) for obj in list_of_queryset]

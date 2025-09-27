
from config.settings.base import ALLOWED_CURRENCIES


class CurrencyValidator:
    
    @staticmethod
    def validate(currency: str) -> str:
        if currency not in ALLOWED_CURRENCIES:
            raise ValueError(f"Currency '{currency}' is not supported. Only {ALLOWED_CURRENCIES}")
        return currency

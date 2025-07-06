# https://medium.com/@bernardonacif/django-criando-e-executando-comandos-dentro-do-projeto-3f7100bc4ac5

import requests
import logging
import time
from datetime import datetime
from rates.models import Rate

logger = logging.getLogger(__name__)

MAX_RETRIES = 2
RETRY_DELAY = 5  

def fetch_and_save_rates(list_dates, base_currency, target_currency):
    all_rates=[]
    for date_str in list_dates:

        result= get_rates_by(date_str,target_currency)

        if result.exists():
            all_rates.extend(result.values('date', 'base', 'currency', 'value'))

        else:
            for attempt in range(MAX_RETRIES):
                try:
                    params={
                            "base": base_currency,
                            "symbols": target_currency,
                            "date": date_str
                        }
                        
                    response = requests.get("https://api.vatcomply.com/rates",params=params)

                    if response.status_code == 200:
                        data = response.json()

                        insert_rate(data)   #insert
                        
                        for currency, value in data["rates"].items():
                            all_rates.append({
                                "date": data["date"],
                                "base": data["base"],
                                "currency": currency,
                                "value": value
                            })
                        break  

                    else:
                        logger.warning(f"Try {attempt + 1}: error to get API. HTTP CODE: {response.status_code}")

                except Exception as e:
                    logger.error(f"Try {attempt + 1}: error to process the request - {e}")
                    continue
                # Aguarda antes de tentar novamente
                if attempt < MAX_RETRIES - 1:
                    logger.warning(f"Awaiting {RETRY_DELAY} seconds for try again...")
                    time.sleep(RETRY_DELAY)
    
    return all_rates

def insert_rate(obj):

    data = obj
    date_str = data["date"]
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()

    base_currency = data["base"]
    rates = data["rates"] #dict

    for currency, value in rates.items():
        
        Rate.objects.update_or_create(
            date=date_obj,
            base=base_currency,
            currency=currency,
            defaults={"value": value}
        )
def get_rates_by(date,currency):
    try:
        rates = Rate.objects.filter(date = date,currency=currency).order_by('-date')
        return rates
    except Rate.DoesNotExist:
        return None

import requests
import time

class ClientVatcomply:
    
    BASE_URL = "https://api.vatcomply.com/rates"

    def __init__(self, base: str , symbols: str , date: str ):
        self.params = {"base": base, "symbols": symbols, "date": date}

    def _get(self, timeout: int = 5, attempts: int = 3):

        for attempt in range(attempts):
            try:
                response = requests.get(self.BASE_URL, params=self.params, timeout=timeout)
                response.raise_for_status()
                return response.json()

            except ValueError:
                raise ValueError("Invalid JSON response from external API")

            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    sleep_time = 0.5 * attempt
                    time.sleep(sleep_time)
                    continue
                else:
                    raise e

            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                time.sleep(1)
                continue

        raise RuntimeError(f"Failed to fetch rates after {attempts} attempts for params={self.params}")

    @classmethod
    def fetch_by_dates(cls, base: str, symbols: str, date_list: list):
        results = []
        for date in date_list:
            client = cls(base=base, symbols=symbols, date=date)
            data = client._get()
            results.append(data)
        return results
                                  

        

        


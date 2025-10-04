import requests
import time

def get_vatcomply_exchange_rates(params):

    for attempt in range(5):          
        try:
            response = requests.get(
                "https://api.vatcomply.com/rates",
                params=params,
                timeout=10
            )
            response.raise_for_status()

            return response

        except ValueError:
            raise ValueError("Error external api: response is not valid JSON")
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                time.sleep(0.5 * (attempt + 1)) 
                continue
            else:
                raise 
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            time.sleep(1)
            continue
    else:
        raise RuntimeError(f"Failed to fetch exchange rate for {params} after multiple attempts")
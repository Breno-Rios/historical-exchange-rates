import requests

import requests

def get_vatcomply_exchange_rates(params):
    try:
        response = requests.get(
            "https://api.vatcomply.com/rates",
            params=params,
            timeout=10 
        )
        response.raise_for_status()

        return response

    except requests.exceptions.Timeout:
        raise("Error external api: connection timed out")

    except ValueError:
        raise("Error external api: response is not valid JSON")

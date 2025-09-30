from django.test import TestCase
import requests

class vatcomplyRates(TestCase):

    def test_api_vatcomply_is_active(self):  
        response = requests.get("https://api.vatcomply.com/rates")
        self.assertEqual(response.status_code, 200)  
              
    def test_api_vatcomply_returns_status_code_200(self):  
        params={
                    "base": 'USD',
                    "symbols": 'BRL',
                    "date": '2025-09-01'
                }
        response = requests.get("https://api.vatcomply.com/rates",params=params)
        self.assertEqual(response.status_code, 200)
                
    def test_api_vatcomply_returns_all_values_of_dict(self):  
        params={
                    "base": 'USD',
                    "symbols": 'BRL',
                    "date": '2025-09-01'
                }
        response = requests.get("https://api.vatcomply.com/rates",params=params)
        data = response.json()

        outp_date= data.get('date')
        outp_base=data.get('base')
        outp_currency=list(data.get('rates').keys())[0]
        outp_value=data.get('rates').get('BRL')

        self.assertEqual(outp_date, "2025-09-01")
        self.assertEqual(outp_base, "USD")
        self.assertEqual(outp_currency, "BRL")
        self.assertIsInstance(outp_value, float)  
        self.assertGreater(outp_value, 0)        
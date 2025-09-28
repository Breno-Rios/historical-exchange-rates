from django.test import TestCase
from django.urls import reverse

import pytest

class test_ExchangeAPIviews(TestCase):

  def test_get_all_currency_exchange_rates_should_return_status_code_200(self):

    url = reverse('api:get_all_currency_exchange_rates')

    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
  def test_get_currency_exchange_rates_by_currency_should_return_status_code_200(self):

    url = reverse('api:get_currency_exchange_rates_by_currency')

    response = self.client.get(url, {'currency-code': 'BRL'})
    
    self.assertEqual(response.status_code, 200)

  def test_get_currency_exchange_rates_by_date_should_return_status_code_200(self):

    url = reverse('api:get_currency_exchange_rates_by_date')

    response = self.client.get(url, {'exchange-date': '2025-09-01'})
    
    self.assertEqual(response.status_code, 200)
  def test_get_currency_exchange_rates_by_data_range_should_return_status_code_200(self):

    url = reverse('api:get_currency_exchange_rates_by_data_range')

    response = self.client.get(url, {'start-date': '2025-09-01','end-date': '2025-09-01'})

    self.assertEqual(response.status_code, 200)


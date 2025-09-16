#https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Server-side/Django/Testing
#https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29623186#overview
from django.test import TestCase
from django.urls import reverse

from rates import views

# Create your tests here.

class RateURLsTest(TestCase):
    def test_rates_home_urls_is_correct(self):
        url= reverse('rates:home')
        self.assertEqual(url,"/")

    def test_rates_rate_graph_urls_is_correct(self):
        url= reverse('rates:rate_graph')
        self.assertEqual(url,"/highcharts/")

    #Endpoints to API
    def test_rates_rate_periods_urls_is_correct(self):
        url= reverse('rates:rate_periods')
        self.assertEqual(url,"/api/rates/period/")

    def test_rates_day_rates_urls_is_correct(self):
        url= reverse('rates:day_rates')
        self.assertEqual(url,"/api/rates/day/")

    def test_rates_rates_for_target_urls_is_correct(self):
        url= reverse('rates:rates_for_target')
        self.assertEqual(url,"/api/rate/")

    def test_rates_all_rates_urls_is_correct(self):
        url= reverse('rates:all_rates')
        self.assertEqual(url,"/api/rates/")
#https://developer.mozilla.org/pt-BR/docs/Learn_web_development/Extensions/Server-side/Django/Testing
#https://www.udemy.com/course/curso-de-django-web-framework-com-python-html-e-css/learn/lecture/29623186#overview
from django.test import TestCase
from django.urls import reverse, resolve

from rates import views

# Create your tests here.

class RateURLsTest(TestCase):
    def test_rates_home_urls_is_correct(self):
        url= reverse('rates:home')
        self.assertEqual(url,"/")

    def test_rates_rate_graph_urls_is_correct(self):
        url= reverse('rates:rate_graph')
        print(url)
        self.assertEqual(url,"/home/api/")

class RateViewsFunctionsTest(TestCase):
    def test_rates_home_url_function_is_correct(self):
        view= resolve(reverse('rates:home'))
        self.assertIs(view.func,views.home)

    def test_rates_rate_graph_url_function_is_correct(self):
        view= resolve(reverse('rates:rate_graph'))
        self.assertIs(view.func,views.call_get_rates)

        

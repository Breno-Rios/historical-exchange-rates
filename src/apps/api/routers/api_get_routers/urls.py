from django.urls import path

from apps.api import views

app_name = 'api'

urlpatterns = [
    path('period/', views.get_currency_exchange_rates_by_data_range, name= "get_currency_exchange_rates_by_data_range"),
    path('date/', views.get_currency_exchange_rates_by_date, name= "get_currency_exchange_rates_by_date"),
    path('exchange-code/', views.get_currency_exchange_rates_by_currency, name= "get_currency_exchange_rates_by_currency"),
    path('', views.get_all_currency_exchange_rates, name= "get_all_currency_exchange_rates"),
]
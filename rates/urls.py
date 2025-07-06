from django.urls import path

from rates.views import home,call_get_rates

urlpatterns = [
    path('', home),
    path('home/', home),
    path('home/api/', call_get_rates)
    
]
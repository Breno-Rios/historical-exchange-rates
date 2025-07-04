from django.urls import path

from rates.views import home

urlpatterns = [
    path('', home),
    path('home/', home)
    
]
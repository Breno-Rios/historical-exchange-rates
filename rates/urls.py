from django.urls import path

from rates import views

app_name = 'rates'

urlpatterns = [
    path('', views.home,name= "home"),
    path('home/api/', views.call_get_rates, name= "rate_graph")
    
]
from django.urls import path

from rates import views

app_name = 'rates'

urlpatterns = [
    path('', views.home,name= "home"),
    path('highcharts/', views.call_get_rates, name= "rate_graph"),

    #New Endpoints
    path('api/rates/period/', views.get_rates_by_range_date, name= "rate_periods"),
    path('api/rates/day/', views.get_rates_by_day, name= "day_rates"),
    path('api/rate/', views.get_rates_by_target, name= "rates_for_target"),
    path('api/rates/', views.get_all_rates, name= "all_rates"),
]
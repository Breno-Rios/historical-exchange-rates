from django.urls import path

from apps.rates import views

app_name = 'rates'

urlpatterns = [
    path('', views.home,name= "home"),
    path('dashboard/', views.dashboard, name= "dashboard"),
]
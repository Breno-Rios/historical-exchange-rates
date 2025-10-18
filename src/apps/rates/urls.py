from django.urls import path

from apps.rates import views

app_name = 'rates'

urlpatterns = [
    #path('', views.HomeView.as_view(),name= "home"),
    path('', views.HomeView.as_view(),name= "home"),
    path('dashboard/', views.DashboardView.as_view(), name= "dashboard"),
]
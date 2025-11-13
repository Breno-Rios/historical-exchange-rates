from django.urls import path
from apps.api import api_views 
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path("rates/", api_views.RateAPIList.as_view()),
    path("rates/<str:start_date>/<str:end_date>/", api_views.RateAPIFilterPeriod.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
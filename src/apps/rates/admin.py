from django.contrib import admin
from apps.rates.models import Rate

# Register your models here.

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ("date", "base", "currency", "value")

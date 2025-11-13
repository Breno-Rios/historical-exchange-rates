from config.settings.base import ALLOWED_CURRENCIES
from rest_framework import serializers
from apps.rates.models import Rate
from datetime import date

class RateSerializerList(serializers.ModelSerializer):
    class Meta:
        model= Rate
        fields = '__all__'

class RateSerializerFilter(serializers.Serializer):
    date = serializers.DateField(required=False,  allow_null=True)
    currency = serializers.CharField(required=False, allow_blank=True)

    def validate_date(self, value):
        if  value and value > date.today():
            raise serializers.ValidationError("date must not be after today")
        value = date.fromisoformat(date.isoformat(value))
        return value
    
    def validate_currency(self, value):
        if value and value not in ALLOWED_CURRENCIES:
            raise serializers.ValidationError(f"Currency '{value}' is not supported. Only {ALLOWED_CURRENCIES}")
        return value
  
class RateSerializerFilterPeriod(serializers.Serializer):
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True) 
    base = serializers.CharField(required=False, allow_blank=True,default="USD")
    currency = serializers.CharField(required=True)

    def validate_start_date(self, value):
        if not value:
            raise ValueError('missing start_date')
        if value > date.today():
            raise serializers.ValidationError("date must not be after today")
        value = date.fromisoformat(date.isoformat(value))
        return value
     
    def validate_end_date(self, value):
        if not value:
            raise ValueError('missing end_date')
        if value > date.today():
            raise serializers.ValidationError("date must not be after today")
        value = date.fromisoformat(date.isoformat(value))
        return value
    
    def validate_currency(self, value):
        if value and value not in ALLOWED_CURRENCIES:
            raise serializers.ValidationError(f"Currency '{value}' is not supported. Only {ALLOWED_CURRENCIES}")
        return value
    


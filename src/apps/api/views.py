from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .utils.exchange_date_formater import DateFormatter

from .services.exchange_rates_services import RateService

from .validators.currency_code_validator import CurrencyValidator

def get_all_currency_exchange_rates(request):
    if request.method == 'GET':
        try:

            content = RateService.get_all_currency_exchange_rates()
            
            return JsonResponse({"data": content}, safe= True, status= 200)
        
        except ObjectDoesNotExist as e:  
            return JsonResponse({"error": str(e)}, status=404)

        except ValueError as e:  
            return JsonResponse({"error": str(e)}, status=400)

        except Exception as e: 
            return JsonResponse({"error": "Unexpected error", "details": str(e)}, status=500)

def get_currency_exchange_rates_by_date(request):
    if request.method == 'GET':
        try:
            exchange_date = DateFormatter.fromisoformat(request.GET.get('exchange-date'))

            if not exchange_date:
                raise ValueError('missing exchange_date param')
            
            content = RateService.get_currency_exchange_rates_by_date(date= exchange_date)
            
            return JsonResponse({"data": content}, status= 200)
        
        except ObjectDoesNotExist as e:  
            return JsonResponse({"error": str(e)}, status=404)

        except ValueError as e:  
            return JsonResponse({"error": str(e)}, status=400)

        except Exception as e: 
            return JsonResponse({"error": "Unexpected error", "details": str(e)}, status=500)

def get_currency_exchange_rates_by_currency(request):
     if request.method == 'GET':
        try:
            currency_code = request.GET.get('currency-code')

            if not currency_code:
                raise ValueError('missing currency_code param')

            currency_code = CurrencyValidator.validate(request.GET.get('currency-code'))

            
            content = RateService.get_currency_exchange_rates_by_currency(target_currency = currency_code)
            
            return JsonResponse({"data": content}, status= 200)
        
        except ObjectDoesNotExist as e:  
            return JsonResponse({"error": str(e)}, status=404)

        except ValueError as e:  
            return JsonResponse({"error": str(e)}, status=400)

        except Exception as e: 
            return JsonResponse({"error": "Unexpected error", "details": str(e)}, status=500)

def get_currency_exchange_rates_by_data_range(request):

    if request.method == 'GET':
        try:
            start_date = DateFormatter.fromisoformat(request.GET.get('start-date'))
            end_date = DateFormatter.fromisoformat(request.GET.get('end-date'))

            if not start_date or not end_date:
                raise ValueError('missing start_date or end_date')
            
            content = RateService.get_currency_exchange_rates_by_data_range(start_date= start_date, end_date= end_date)

            return JsonResponse({"data": content}, status= 200)
        
        except ObjectDoesNotExist as e:  
            return JsonResponse({"error": str(e)}, status=404)

        except ValueError as e:  
            return JsonResponse({"error": str(e)}, status=400)

        except Exception as e: 
            return JsonResponse({"error": "Unexpected error", "details": str(e)}, status=500)
        

    

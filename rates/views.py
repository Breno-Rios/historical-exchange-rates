from django.shortcuts import render
from django.http import JsonResponse
from rates.service import fetch_and_save_rates
from rates.utils import generate_date_range


# Create your views here.
def home(request):
  return render(request,'rates/home.html')


def call_get_rates(request):
    try:
        start_date = request.GET.get('start-date')
        end_date = request.GET.get('end-date')
        base_currency = request.GET.get('base-currency')
        target_currency = request.GET.get('target-currency')

        if not all([start_date, end_date, base_currency, target_currency]):
            return JsonResponse({'error': 'Required parameters missing'}, status=400)
    
        list_dates = generate_date_range(start_date, end_date)

        # chama o service
        data = fetch_and_save_rates(list_dates, base_currency, target_currency)  
        
        base = [ item['base']  for item in data ]
        dates = [ item['date']  for item in data ]
        currency= [ item['currency'] for item in data ]
        values= [ item['value'] for item in data ]

        context = {
            'base': base,
            'currency': currency,
            'categories':dates,
            'values': values,
        }

        return render(request, 'rates/home.html', context)
    
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)

def get_rates_by_range_date(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if not all([start_date, end_date]):
        return JsonResponse({'error': 'Required parameters missing'}, status=400)
    try:
        return JsonResponse({"message": "range"}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_rates_by_target(request):
    target = request.GET.get('target')
    if not all([target]):
        return JsonResponse({'error': 'Required parameters missing'}, status=400)
    try:
        return JsonResponse({"message": "target"}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_rates_by_day(request):
    start_date = request.GET.get('start_date')
    if not all([start_date]):
        return JsonResponse({'error': 'Required parameters missing'}, status=400)
    try:
        return JsonResponse({"message": "day"}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_all_rates(request):
    try:
        return JsonResponse({"message": "all"}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
import json
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
        if target_currency not in ['JPY', 'BRL', 'EUR'] or base_currency != 'USD':
            return JsonResponse({'error': 'Incorrect Parameters'}, status=400)
        list_dates = generate_date_range(start_date, end_date)

        if not isinstance(list_dates, list):
            return JsonResponse({'error': str(list_dates)}, status=400)
        
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


    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 
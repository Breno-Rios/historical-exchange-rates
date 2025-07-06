import logging
from django.shortcuts import render
from django.http import JsonResponse
from rates.service import fetch_and_save_rates
from datetime import datetime,timedelta


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
            return JsonResponse({'error': 'Parâmetros obrigatórios faltando'}, status=400)

        list_dates = generate_date_range(start_date, end_date)

        if not isinstance(list_dates, list):
            return JsonResponse({'error': str(list_dates)}, status=500)
        
        # chama o service para criarist_datesist_datesist_datesist_datesist_dates
        msg = fetch_and_save_rates(list_dates, base_currency, target_currency)
        return JsonResponse({"message": msg})


    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 

def generate_date_range(start_date, end_date):
    try:
        # change as strings to obj date
        fmt = "%Y-%m-%d"
        start = datetime.strptime(start_date, fmt).date()
        end    = datetime.strptime(end_date,    fmt).date()

        if start > end:
            return "The end_date cannot be earlier than the start_date"
        
        date_list = []
        current_date = start

        while current_date <= end:
            date_list.append(current_date.isoformat())  # 'YYYY-MM-DD'
            current_date += timedelta(days=1)

        return date_list
            
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500) 
    
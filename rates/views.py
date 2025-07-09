from django.shortcuts import render
from django.http import JsonResponse
from rates import service
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
        data = service.fetch_and_save_rates(list_dates, base_currency, target_currency)  
        
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
        data= service.get_by_range(start_date,end_date)
        return JsonResponse({'data':data}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_rates_by_target(request):
    target = request.GET.get('target')
    if not target:
        return JsonResponse({'error': 'Required parameters missing'}, status=400)
    try:
        data = service.get_by_target(target)
        return JsonResponse({'data':data}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_rates_by_day(request):
    start_date = request.GET.get('start_date')
    if not start_date:
        return JsonResponse({'error': 'Required parameters missing'}, status=400)
    try:
        data = service.get_by_day(start_date)
        return JsonResponse({'data':data}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
    
def get_all_rates(request):
    try:
        data = service.get_all()
        return JsonResponse({'data':data}, status=200)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except Exception as e:
        return JsonResponse({'error': 'Internal server error'}, status=500)
from .forms import RateForms

from config.settings.base import ALLOWED_CURRENCIES

from django.http import JsonResponse
from datetime import date

from apps.api.serializers.exchange_rates_serializer import ExchangeRatesSerializer
from apps.api.services.exchange_rates_services import RateService
from apps.api.repository.rate_repository import RateRepository

from requests.exceptions import Timeout, ConnectionError, HTTPError
from django.core.exceptions import ObjectDoesNotExist

from django.views.generic import TemplateView , View


class HomeView(TemplateView):
    template_name = "rates/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RateForms()
        return context

class DashboardView(View):
    service = RateService(RateRepository())
    serializer = ExchangeRatesSerializer()

    def json_error(self, message, status=400):
        return JsonResponse({"error": message}, status=status)
    
    def get_validated_params(self, request):
            
        start_date = request.GET.get('start-date')
        end_date = request.GET.get('end-date')
        currency_code = request.GET.get('currency-code')

        if not start_date or not end_date:
            raise ValueError('missing start_date or end_date')
        if not currency_code:
            raise ValueError('missing currency_code param')

        if currency_code not in ALLOWED_CURRENCIES:
            raise ValueError(f"Currency '{currency_code}' is not supported. Only {ALLOWED_CURRENCIES}")
        
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)

        return start_date, end_date, currency_code
         
    
    def get(self, request, *args, **kwargs):
        try:
            start_date, end_date, currency_code = self.get_validated_params(request)
                
            queryset = self.service.get_dashboard_currency_exchange_rates(
                start_date= start_date,
                end_date= end_date,
                base_currency='USD',
                target_currency=currency_code
            )
            content = self.serializer.list_to_dict(queryset)
            return JsonResponse({"data": content}, status=200)

        except Timeout as e:
            return self.json_error("Timeout contacting external API",504)

        except ConnectionError as e:
            return self.json_error("Could not connect to external API",503)

        except HTTPError as e:
            return self.json_error("HTTP error from external API",502)

        except ObjectDoesNotExist as e:
            return self.json_error(str(e),404)

        except ValueError as e:
            return self.json_error(str(e),400)

        except RuntimeError as e:  
            return self.json_error(str(e),500)

        except Exception as e:
            return self.json_error(f"Unexpected error {str(e)}",500)
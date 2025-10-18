from .forms import RateForms
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from apps.utils.exchange_date_formater import DateFormatter

from apps.api.services.exchange_rates_services import RateService

from apps.api.validators.currency_code_validator import CurrencyValidator

from apps.api.serializers.exchange_rates_serializer import ExchangeRatesSerializer

from requests.exceptions import Timeout, ConnectionError, HTTPError

from django.views.generic import TemplateView , View


class HomeView(TemplateView):
    template_name = "rates/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RateForms()
        return context

class DashboardView(View):
    service = RateService()
    serializer = ExchangeRatesSerializer()

    def validate_params(self):
            
        start_date = self.request.GET.get('start-date')
        end_date = self.request.GET.get('end-date')
        currency_code = self.request.GET.get('currency-code')

        if not start_date or not end_date:
            raise ValueError('missing start_date or end_date')
        if not currency_code:
            raise ValueError('missing currency_code param')
        
        start_date = DateFormatter.fromisoformat(start_date)
        end_date = DateFormatter.fromisoformat(end_date)
        currency_code = CurrencyValidator.validate(currency_code)

        return start_date, end_date, currency_code
    
    def get(self, request, *args, **kwargs):
        try:
            start_date, end_date, currency_code = self.validate_params()
              
            queryset = self.service.get_dashboard_currency_exchange_rates(
                start_date=start_date,
                end_date=end_date,
                base_currency='USD',
                target_currency=currency_code
            )
            content = self.serializer.list_to_dict(queryset)
            return JsonResponse({"data": content}, status=200)

        except Timeout as e:
            return JsonResponse(
                {"error": "Timeout contacting external API",
                    "details": str(e)},
                status=504
            )

        except ConnectionError as e:
            return JsonResponse(
                {"error": "Could not connect to external API",
                    "details": str(e)},
                status=503
            )

        except HTTPError as e:
            return JsonResponse(
                {"error": "HTTP error from external API", "details": str(e)},
                status=502
            )

        except ObjectDoesNotExist as e:
            return JsonResponse({"error": str(e)}, status=404)

        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

        except RuntimeError as e:  # falha do retry do service
            return JsonResponse({"error": str(e)}, status=500)

        except Exception as e:
            return JsonResponse({"error": f"Unexpected error {str(e)}"}, status=500)
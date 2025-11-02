from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api.services.exchange_rates_services import RateService
from apps.api.repositories.rate_repository import RateRepository
from apps.api.serializers.api_serializer import RateSerializerList, RateSerializerFilter, RateSerializerFilterPeriod

class RateAPIList(APIView):
    repository = RateRepository()
    service = RateService(repository) 

    def get(self, request, format = None):
        try:
            rates = self.service.find_all()
            serializer = RateSerializerList(rates, many = True)
            return(Response(serializer.data, status=status.HTTP_200_OK))

        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": "Unexpected error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class RateAPIFilter(APIView):
    repository = RateRepository()
    service = RateService(repository) 
      
    def get(self, request, format = None):
        try:

            serializer = RateSerializerFilter(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            
            filters = serializer.validated_data
            rate = self.service.find_by(**filters)
            serializer = RateSerializerFilter(rate, many = True)

            return(Response(serializer.data, status=status.HTTP_200_OK))
        
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
                
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": "Unexpected error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RateAPIFilterPeriod(APIView): 
    repository = RateRepository()
    service = RateService(repository) 
      
    def get(self, request, format = None):
        try:
            serializer = RateSerializerFilterPeriod(data=request.query_params)
            serializer.is_valid(raise_exception=True)
            
            filters = serializer.validated_data
            rate = self.service.find_by_data_range_and_filters(**filters)
            serializer = RateSerializerFilterPeriod(rate, many = True)

            return(Response(serializer.data, status=status.HTTP_200_OK))
        
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": "Unexpected error", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from ledger.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def sales(request):
    Processing().pre_sales()
    return JsonResponse({'SALES': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def cost(request):
    Processing().pre_cost()
    return JsonResponse({'COST': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def upload_sales(request):
    Processing().insert_sales()
    return JsonResponse({'insert_sales': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def upload_cost(request):
    Processing().insert_cost()
    return JsonResponse({'insert_cost': 'SUCCESS'})

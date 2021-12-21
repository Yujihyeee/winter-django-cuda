from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from ledger.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def preprocess(request):
    Processing().pre_process()
    return JsonResponse({'Pre-Processing': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    Processing().insert_data()
    return JsonResponse({'insert_data': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def cost(request):
    Processing().insert_cost()
    return JsonResponse({'insert_cost': 'SUCCESS'})

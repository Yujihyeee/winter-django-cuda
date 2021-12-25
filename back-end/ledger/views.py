import datetime

from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from ledger.models import Ledger
from ledger.models_process import Processing
from ledger.serializer import LedgerSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_sales(request):
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


@api_view(['GET'])
@parser_classes([JSONParser])
def sales(request, pk):
    Processing().sales_process(pk)
    return JsonResponse({'SALES': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def profit(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    c = '매출액'
    sum_data = Ledger.objects.filter(category=c).aggregate(Sum('price'))
    report = {"report": sum_data}
    return JsonResponse(data=report, safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def profit_month(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    sum_data = Ledger.objects.filter(date__year=2021, date__month=request.data).aggregate(Sum('price'))
    report = {"report": sum_data}
    return JsonResponse(data=report, safe=False)

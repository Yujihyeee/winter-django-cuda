from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from ledger.models import Ledger
from ledger.models_process import Processing


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
def sales(request):
    Processing().sales_process()
    return JsonResponse({'SALES': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def profit(request):
    y = Ledger.objects.filter(year=2021)
    c = y.filter(category='매출액')
    sum_data = c.aggregate(Sum('price'))
    return JsonResponse(data=sum_data, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def report_process(request):
    Processing().report_process()
    return JsonResponse({'report_process': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def show_6month_cost(request):
    result = Processing().show_cost()
    result = result[6:12]
    print(result)
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def month_cost(request):
    result = Processing().show_cost()
    result = result[11]
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def year_profit(request):
    print('#################################')
    result = Processing().year_profit()
    print('#################################')
    print(result)
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def insert(request):
    Processing().insert()
    return JsonResponse({'insert': 'SUCCESS'})

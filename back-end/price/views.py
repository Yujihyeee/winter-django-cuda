from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from price.models import Price
from price.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_price(request):
    Processing().price_process()
    return JsonResponse({'PRICE': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def get_price(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    print('=========================')
    report = request.data
    print(report)
    arr = report[0]
    print('=========================')
    print(arr)
    dic = arr[0]
    print('=========================')
    print(dic)
    a = dic
    b = dic['day']
    print(dic['plane'])
    print('=========================')
    price = Price.objects.filter(category='plane', category_id__in=dic['plane']).values(['price'])
    # activity = report[0][3]
    print(price)
    return JsonResponse(data=price, safe=False)

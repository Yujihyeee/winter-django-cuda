from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
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
    report = request.data[{'report': 'people'}, {'report': 'days'}, {'plane': 'id'}, {'acc': 'id'}, {'activity': 'id'}]
    return JsonResponse(data=report, safe=False)

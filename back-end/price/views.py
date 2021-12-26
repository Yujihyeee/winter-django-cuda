from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from ledger.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_sales(request):
    Processing().pre_sales()
    return JsonResponse({'SALES': 'SUCCESS'})

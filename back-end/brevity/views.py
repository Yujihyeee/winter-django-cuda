from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from brevity.models_data import DbUploader


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_process(request):
    DbUploader().pre_process()
    return JsonResponse({'preprocessing': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCESS'})


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def process(request):
#     DbUploader().process()
#     return JsonResponse({'process': 'SUCCESS'})

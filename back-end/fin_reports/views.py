from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from fin_reports.models import FinReports
from fin_reports.models_data import DbUploader
from fin_reports.serializers import FinReportsSerializer
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


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


@api_view(['POST'])
@parser_classes([JSONParser])
def find_by_detail(request):
    print('############ 2 ##########')
    quest = request.data
    print(quest)
    answer = FinReports.objects\
        .filter(symptom=quest['symptom'], details=quest['details']).get()
        # .only('symptom', 'level', 'answer')
    serializer = FinReportsSerializer(answer)
    return JsonResponse(data=serializer.data, safe=False)

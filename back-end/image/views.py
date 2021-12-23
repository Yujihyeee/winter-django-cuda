from django.shortcuts import render
import os

from image.model_all_data import AllDbUploader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()
# Create your views here.
from django.http import JsonResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes

from image.models_data import DbUploader


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    print('############ 1 ##########')
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCESS'})

@api_view(['PUT'])
@parser_classes([JSONParser])
def all_upload(request):
    print('############ 1 ##########')
    AllDbUploader().insert_db_data()
    return JsonResponse({'DB Upload': 'SUCCESS'})
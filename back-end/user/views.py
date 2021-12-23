from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions, generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from user.model_data import DbUploader
from user.models import User
from user.serializers import UserSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    print('############ 1 ##########')
    DbUploader().insert_data()
    return JsonResponse({'Product Upload': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def get_mbti(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    user_data = User.objects.filter()
    user_data = UserSerializer(user_data, many=True).data
    report = {"report": user_data}
    return JsonResponse(data=report, safe=False)



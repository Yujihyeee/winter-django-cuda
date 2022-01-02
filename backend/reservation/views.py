from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from reservation.models_process import Processing
from reservation.serializers import ReservationSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def preprocess(request):
    Processing().pre_process()
    return Response({'preprocess': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request, pk):
    Processing().process(pk)
    return JsonResponse({'process': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_data(request):
    Processing().insert_data()
    return Response({'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def profit_year(request):
    result = Processing().year()
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def profit_month(request):
    result = Processing().year()
    result = result[11]
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def profit_6month(request):
    result = Processing().year()
    print(result)
    result = result[6:12]
    return JsonResponse(data=result, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def count_res(request):
    count_data = Processing().count()
    return JsonResponse(data=count_data, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def recent(request):
    result = Processing().recent()
    recent_data = ReservationSerializer(result, many=True).data
    return JsonResponse(data=recent_data, safe=False)


@api_view(['GET'])
@parser_classes([JSONParser])
def dummy_sales(request):
    Processing().dummy_sales()
    return Response({'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_test(request):
    Processing().insert_test()
    return Response({'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def sum(request):
    Processing().sum()
    return Response({'SUCCESS'})

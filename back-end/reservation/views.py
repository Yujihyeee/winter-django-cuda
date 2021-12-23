from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from reservation.models import Reservation
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


@api_view(['POST'])
@parser_classes([JSONParser])
def show_invoice(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    invoice_data = Reservation.objects.all()
    invoice_data = ReservationSerializer(invoice_data, many=True).data
    report = {"report": invoice_data}
    return JsonResponse(data=report, safe=False)


# @api_view(['POST'])
# @parser_classes([JSONParser])
# def show_chart(request):
#     print(f'hi : {request}')
#     print(f'hello : {request.data}')
#     chart2_data = Reservation.objects.all()
#     invoice_data = ReservationSerializer(invoice_data, many=True).data
#     report = {"report": invoice_data}
#     return JsonResponse(data=report, safe=False)

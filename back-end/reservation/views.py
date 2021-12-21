from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from reservation.models import Reservation
from reservation.models_process import Processing
from reservation.serializers import ReservationSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def preprocess(request):
    Processing().pre_process(p=1)
    return Response({'preprocess': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_data(request):
    Processing().insert_data()
    return Response({'SUCCESS'})
    # if request.method == 'GET':
    #     queryset = Reservation.objects.all()
    #     serializer = ReservationSerializer(queryset, many=True)
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = ReservationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATE)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def process(request):
#     Processing().process()
#     return JsonResponse({'Processing': 'SUCCESS'})


# @api_view(['POST'])
# @parser_classes([JSONParser])
# def process(request):
#     try:
#         loginUser = request.data
#         dbUser = Brevity.objects.get(pk=loginUser['username'])
#         if loginUser['password'] == dbUser.password:
#             userSerializer = UserSerializer(dbUser, many=False)
#             ic(userSerializer)
#             return JsonResponse(data=userSerializer.data, safe=False)
#         else:
#             print('******** 비밀번호 오류')
#             return JsonResponse(data={'result': 'PASSWORD-FAIL'}, status=201)
#
#     except User.DoesNotExist:
#         print('*' * 50)
#         print('******** Username 오류')
#         return JsonResponse(data={'result': 'USERNAME-FAIL'}, status=201)

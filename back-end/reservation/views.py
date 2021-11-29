from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from brevity.models import Brevity
from reservation.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def preprocess(request):
    Processing().pre_process()
    return JsonResponse({'Pre-Processing': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def insert_reservation(request):
    Processing().insert_reservation(arr=[])
    return JsonResponse({'Processing': 'SUCCESS'})


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

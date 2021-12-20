from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from jeju_data.models import Plane, Accommodation
from jeju_data.serializer import PlaneSerializer, AccommodationSerializer
from jeju_schedule.models_data import DbUploader


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def pre_process(request):
#     DbUploader().pre_process()
#     return JsonResponse({'preprocessing': 'SUCCESS'})
from jeju_schedule.models_process import JejuProcess


@api_view(['GET'])
@parser_classes([JSONParser])
def upload(request):
    DbUploader().insert_data()
    return JsonResponse({'Data Uploading': 'SUCCESS'})


# @api_view(['GET'])
# @parser_classes([JSONParser])
# def process(request):
#     DbUploader().process()
#     return JsonResponse({'process': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def recommendation(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    print('############ 1 ##########')
    jeju = JejuProcess(request.data)
    mbti = jeju.mbti_set()
    print('############ 2 ##########')
    plane = jeju.plane()
    departure_plane = plane[0]
    arrival_plane = plane[1]
    print('############ 3 ##########')
    accommodation = jeju.accommodation(mbti)
    print(accommodation)
    print('############ 4 ##########')
    activity = jeju.activity(mbti)
    print(activity)
    print(activity)
    print('############ 5 ##########')
    if jeju.olle() == 0:
        return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data), safe=False)
    else:
        if jeju.olle()[0] == None :
            oleum = jeju.olle()[1]
            print(oleum)
            print('############ 6 ##########')
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, oleum.data), safe=False)
        if jeju.olle()[1] == None :
            olle = jeju.olle()[0]
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, olle.data), safe=False)
        else:
            oleum = jeju.olle()[1]
            olle = jeju.olle()[0]
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, olle.data, oleum.data), safe=False)

    # return JsonResponse(recommendation)
    # return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, olle.data, oleum.data), safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def days(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    print('############ 1 ##########')
    jeju = JejuProcess(request.data)
    print('############ 2 ##########')
    days = jeju.process_days(request.data)
    print('############ 3 ##########')
    print(days[0])   # dic
    print('############ 4 ##########')
    plane_data = Plane.objects.filter(id__in=days[1]).values()
    plane_data = PlaneSerializer(plane_data, many=True).data
    plane = {"plane" : plane_data}
    print(days[1])  # plane
    print(plane)
    print('############ 5 ##########')
    print(days[2])
    acc_data = Accommodation.objects.filter(id=days[2]).values()
    print(acc_data)
    acc_data = AccommodationSerializer(acc_data, many=True).data
    print(acc_data)
    print(days[2])  # acc
    acc = {"acc": acc_data}  # acc
    print(acc)
    print('############ 6 ##########')

    return JsonResponse(data=(plane, acc, days[0]), safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def save_days(request):
    print(f'hi : {request}')
    print(f'hello : {request.data}')
    print('############ 1 ##########')
    jeju = JejuProcess(request.data)
    print('############ 2 ##########')
    days = jeju.process_save_days(request.data)
    print('############ 3 ##########')
    print(days[0])   # dic
    print('############ 4 ##########')
    plane_data = Plane.objects.filter(id__in=days[1]).values()
    plane_data = PlaneSerializer(plane_data, many=True).data
    plane = {"plane" : plane_data}
    print(days[1])  # plane
    print(plane)
    print('############ 5 ##########')
    acc_data = Accommodation.objects.filter(id=days[2]).values()
    acc_data = AccommodationSerializer(acc_data, many=True).data
    print(days[2])  # acc
    acc = {"acc": acc_data}  # acc
    print(acc)
    print('############ 6 ##########')
    activity = {"activity" : days[3]}
    print(days[3])  # activity
    print(activity)
    print('############ 7 ##########')
    restaurant = {"restaurant" : days[4]}
    print(days[4])  # except_restaurant_id
    print(restaurant)
    print('############ 8 ##########')
    tourism = {"tourism" : days[5]}
    print(days[5])  # except_tourism_id
    print(tourism)
    print('############ 9 ##########')
    shop = {"shop" : days[6]}
    print(days[6])  # except_shop_id
    print(shop)
    print('############ 10 ##########')
    startday = days[7]
    endday = days[8]
    day = days[9]
    people = days[10]
    user = days[11]
    print(user)
    relationship = days[12]
    print(len(days))
    if len(days) == 13:
        return JsonResponse(data=(days[0], plane, acc, activity, restaurant, tourism, shop, startday, endday, day, people, user, relationship),safe=False)

    if len(days) == 14:
        print('############ 11 ##########')
        print(days[13])  # olle
        olle = {"olle" : days[13]}
        print(olle)
        return JsonResponse(data=(days[0], plane, acc, activity, olle, restaurant, tourism, shop, startday, endday, day, people, user, relationship), safe=False)
    
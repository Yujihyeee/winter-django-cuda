import datetime
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from jeju.model_data import DbUploader
from jeju.models import JejuSchedule
from jeju.models_process import JejuProcess
from jeju.serializer import JejuSerializer
from jeju_data.models import Plane, Accommodation
from jeju_data.serializer import PlaneSerializer, AccommodationSerializer


@api_view(['POST'])
@parser_classes([JSONParser])
def recommendation(request):
    jeju = JejuProcess(request.data)
    mbti = jeju.mbti_set()
    plane = jeju.plane()
    departure_plane = plane[0]
    arrival_plane = plane[1]
    accommodation = jeju.accommodation(mbti)
    activity = jeju.activity(mbti)
    if jeju.olle() == 0:
        return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data), safe=False)
    else:
        if jeju.olle()[0] == None :
            oleum = jeju.olle()[1]
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, oleum.data), safe=False)
        if jeju.olle()[1] == None :
            olle = jeju.olle()[0]
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, olle.data), safe=False)
        else:
            oleum = jeju.olle()[1]
            olle = jeju.olle()[0]
            return JsonResponse(data=(departure_plane.data, arrival_plane.data, accommodation.data, activity.data, olle.data, oleum.data), safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def days(request):
    jeju = JejuProcess(request.data)
    days = jeju.process_days(request.data)
    plane_data = Plane.objects.filter(id__in=days[1]).values()
    plane_data = PlaneSerializer(plane_data, many=True).data
    plane = {"plane" : plane_data}
    acc_data = Accommodation.objects.filter(id=days[2]).values()
    acc_data = AccommodationSerializer(acc_data, many=True).data
    acc = {"acc": acc_data}
    return JsonResponse(data=(plane, acc, days[0]), safe=False)


@api_view(['POST'])
@parser_classes([JSONParser])
def save_days(request):
    jeju = JejuProcess(request.data)
    days = jeju.process_save_days(request.data)
    plane_data = Plane.objects.filter(id__in=days[1]).values()
    plane_data = PlaneSerializer(plane_data, many=True).data
    plane = {"plane" : plane_data}
    acc_data = Accommodation.objects.filter(id=days[2]).values()
    acc_data = AccommodationSerializer(acc_data, many=True).data
    acc = {"acc": acc_data}  # acc
    activity = {"activity" : days[3]}
    restaurant = {"restaurant" : days[4]}
    tourism = {"tourism" : days[5]}
    shop = {"shop" : days[6]}
    startday = days[7]
    endday = days[8]
    day = days[9]
    people = days[10]
    user = days[11]
    relationship = days[12]
    if len(days) == 13:
        return JsonResponse(data=(days[0], plane, acc, activity, restaurant, tourism, shop, startday, endday, day, people, user, relationship),safe=False)

    if len(days) == 14:
        olle = {"olle" : days[13]}
        return JsonResponse(data=(days[0], plane, acc, activity, olle, restaurant, tourism, shop, startday, endday, day, people, user, relationship), safe=False)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def list_by_user(request, user_id):
    jejuSchedule = JejuSchedule.objects.filter(user_id=user_id)
    serializer = JejuSerializer(jejuSchedule, many=True)
    return JsonResponse(data = serializer.data, safe=False)


@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def list_by_user_pr(request, user_id):
    today = datetime.date.today()
    jejuSchedule = JejuSchedule.objects.raw(
        f"select * from jeju_schedule where user_id = {user_id} and startday > '{today}';")
    serializer = JejuSerializer(jejuSchedule, many=True)
    return JsonResponse(data=serializer.data, safe=False)


@api_view(['DELETE'])
@parser_classes([JSONParser])
def del_list_by_user(request, pk):
    print("********** remove **********")
    print(f'pk : {pk}')
    jejuSchedule = JejuSchedule.objects.get(pk=pk)
    jejuSchedule.delete()
    return JsonResponse({'User want JejuSchedule': 'DELETE SUCCESS'})


@api_view(['PUT'])
@parser_classes([JSONParser])
def dday_up(request):
    DbUploader().updata_jeju_dday()
    return JsonResponse({"JEJU_dday DATA UPLOADED": "SUCCESSFULY!"})

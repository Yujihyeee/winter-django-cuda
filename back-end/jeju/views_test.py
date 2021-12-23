import random
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from icecream import ic
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

# Create your views here.
from jeju_data.models import Plane, PlaneCategory
from user.models import User


@api_view(['POST'])
@parser_classes([JSONParser])
def test_process(request):
    print('############ 1 ##########')
    a = test_option(request)
    print('############ 2 ##########')
    test_user(a)
    print('############ 3 ##########')
    print('############ 4 ##########')
    print('############ 5 ##########')
    print('############ 6 ##########')
    print('############ 7 ##########')
    print('############ 8 ##########')
    print('############ 9 ##########')

    return JsonResponse({'Product test_process': 'SUCCESS'})


def test_option(request):
    # option = {"date1": '2021-05-21', "date2": '2021-06-19', 'start': 'gmp', 'Number': 4, 'user': 15, 'relationship': 'family' }

    # startday = datetime.strptime(option.data['date1'], '%Y-%m-%d')
    # startloc = option.data['start']
    # endday = datetime.strptime(option.data['date2'], '%Y-%m-%d')
    # days = endday - startday
    # people = option.data['Number']
    # user = option.data['user']
    # mbti = User.objects.get(id=option.data['user'])
    # month = option.data['date'][2]
    # relationship = option.data['relationship']

    option = request.data
    startday = datetime.strptime(option['date1'], '%Y-%m-%d')
    startloc = option['start']
    endday = datetime.strptime(option['date2'], '%Y-%m-%d')
    days = endday - startday
    people = option['Number']
    user = User.objects.filter(id=option['user']).values()[0]
    mbti = user['mbti']
    mbti_list = user['mbti_list']
    month = startday.month
    relationship = option['relationship']
    return startday, startloc, endday, days, people, user, mbti, mbti_list, month, relationship

@api_view(['GET'])
@parser_classes([JSONParser])
def test_plane(request):
    return JsonResponse({'Product test_plane': 'SUCCESS'})


def test_plane_set(request):
    option = request.data
    print('*' * 100)
    print(option)
    print('*' * 100)

    startday = datetime.strptime(option['date1'], '%Y-%m-%d')
    startloc = option['start']
    endday = datetime.strptime(option['date2'], '%Y-%m-%d')
    days = endday - startday
    people = option['Number']
    user = option['user']
    mbti = User.objects.get(id=option['user'])
    month = startday.month
    relationship = option['relationship']

    #plane

    # category = PlaneCategory.objects.get(type__icontains='gmp')
    category1 = PlaneCategory.objects.filter(type__istartswith=startloc).values()[0]
    category2 = PlaneCategory.objects.filter(type__iendswith=startloc).values()[0]
    ic(category1['id'])

    nofamily = Plane.objects.filter(plane_category_id=category1['id'], depPlandTime__hour__in=[6, 7, 8, 9, 10]).exclude(airlineNm='AAR' or 'KAL')
    nols, yesls = [], []
    # [nols.append(i.values()) for i in nofamily.values('id')]
    [nols.append(i['id']) for i in nofamily.values('id')]
    # print(nols)
    [print(i) for i in nols]
    # print(nols[random.randint(0, len(nols))])
    # print(nols[random.randint(0, len(nols)-1)])
    departure = {"departure" : random.sample(nols, 3)}
    ic(random.sample(nols, 3))
    nofamily = Plane.objects.filter(plane_category_id=category2['id'], depPlandTime__hour__in=[18, 19, 20, 21]).exclude(
        airlineNm='AAR' or 'KAL')
    [nols.append(i['id']) for i in nofamily.values('id')]
    [print(i) for i in nols]
    arrival = {"arrival" : random.sample(nols, 3)}
    print(departure, arrival)


    # family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category['id'], depPlandTime__hour__in=[8, 9, 10, 11])
    # [yesls.append(i['id']) for i in family.values('id')]
    # [print(i) for i in yesls]
    # print(yesls[random.randint(0, len(yesls)-1)])

    return JsonResponse({'Product test_plane': 'SUCCESS'})

@api_view(['POST'])
@parser_classes([JSONParser])
def test_user(request):
    e, s, t, j = test_user_set(request)
    return JsonResponse({'e': e, 's': s, 't': t, 'j': j })

def test_user_set(request):
    # user
    mbti_list = test_option(request)
    e = mbti_list.count('e')
    s = mbti_list.count('s')
    t = mbti_list.count('t')
    j = mbti_list.count('j')

    return e, s, t, j

@api_view(['POST'])
@parser_classes([JSONParser])
def recommendation(request):
    mbti_list = test_option(request)
    e = mbti_list.count('e')
    s = mbti_list.count('s')
    t = mbti_list.count('t')
    j = mbti_list.count('j')

    return e, s, t, j
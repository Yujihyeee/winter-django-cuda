import math

import pandas as pd
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes

from price.models import Price
from price.models_process import Processing


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_price(request):
    Processing().price_process()
    return JsonResponse({'PRICE': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def get_price(request):
    report = request.data
    arr = report[0]
    dic = arr[0]
    plane_price = {"plane_price": Price.objects.filter(category_id__in=dic['plane'], category='plane').aggregate(Sum('price'))['price__sum']}
    print(plane_price)
    people = dic['people']
    print(people)
    acc_price = {'acc_price': Price.objects.filter(category_id__in=dic['acc_id'], category='accommodation').aggregate(Sum('price'))['price__sum']}
    print(acc_price)
    day = dic['day']
    print(day)
    act_price = {'act_price': Price.objects.filter(category_id__in=dic['activity'], category='activity').aggregate(Sum('price'))['price__sum']}
    print(act_price)
    unit = dic['acc_id'].values('standard_number')
    print(people / unit)
    accommo_price = math.ceil(people / unit) * acc_price[''] * day
    print(accommo_price)
    # reg_date = pr.reg_date.date()
    # price = (plane_price * people) + acc_price + act_price
    # tax = price * 0.1
    # subtotal = price + tax
    # fee = subtotal * 0.2
    # total_price = subtotal + fee
    # jeju_schedule_id = dic['id']
    # arr.append(reg_date)
    # arr.append(people)
    # arr.append(day)
    # arr.append(plane_price)
    # arr.append(acc_price.price)
    # arr.append(act_price)
    # arr.append(price)
    # arr.append(int(tax))
    # arr.append(int(subtotal))
    # arr.append(int(fee))
    # arr.append(int(total_price))
    # arr.append(jeju_schedule_id)
    # n = 12
    # result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
    # df = pd.DataFrame(result, columns=['reg_date', 'people', 'day', 'plane_pr', 'acc_pr', 'act_pr', 'price', 'tax',
    #                                    'subtotal', 'fees', 'total_price', 'jeju_schedule_id'])
    # df.to_csv('reservation/data/get_price.csv')

    return JsonResponse(data=(plane_price, acc_price, act_price), safe=False)

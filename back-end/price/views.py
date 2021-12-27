import pandas as pd
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from price.models import Price
from price.models_process import Processing
from reservation.models import Reservation


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_price(request):
    Processing().price_process()
    return JsonResponse({'PRICE': 'SUCCESS'})


# unit = dic['acc_id'].values('standard_number')
    # print(people / unit)   math.ceil(people / unit)


@api_view(['POST'])
@parser_classes([JSONParser])
def get_price(request):
    report = request.data
    arr = report[0]
    dic = arr[0]
    plane_unit = {"plane_unit": Price.objects.filter(category_id__in=dic['plane'], category='plane').aggregate(Sum('price'))['price__sum']}
    people = {'people': dic['people']}
    plane_price = {'plane_price': plane_unit['plane_unit'] * people['people']}
    acc_unit = {'acc_unit': Price.objects.filter(category='accommodation', category_id=dic['acc_id']).values()[0]['price']}
    day = {'day': dic['day']}
    acc_price = {'acc_price': acc_unit['acc_unit'] * day['day']}
    act_unit = {'act_unit': Price.objects.filter(category_id__in=dic['activity'], category='activity').aggregate(Sum('price'))['price__sum']}
    reg_date = {'reg_date': dic['reg_date']}
    date = {'reg_date': reg_date['reg_date'][:10]}
    price = {'price': plane_price['plane_price'] + acc_price['acc_price'] + act_unit['act_unit']}
    tax = {'tax': int(price['price'] * 0.1)}
    subtotal = {'subtotal': int(price['price'] + tax['tax'])}
    fee = {'fee': int(subtotal['subtotal'] * 0.2)}
    total_price = {'total_price': int(subtotal['subtotal'] + fee['fee'])}
    jeju_schedule_id = {'jeju_schedule_id': dic['id']}
    keys = []
    items = []
    for i in [date, people, day, plane_unit, acc_unit, act_unit, plane_price, acc_price, price, tax, subtotal, fee, total_price, jeju_schedule_id]:
        for j in i:
            keys.append(j)
            items.append(i[j])
    result = dict(zip(keys, items))
    # df = pd.DataFrame(result, index=['0'])
    # print(df)
    # reservation = Reservation.objects.create(reg_date=df['reg_date'],
    #                                          people=df['people'],
    #                                          day=df['day'],
    #                                          plane_pr=df['plane_price'],
    #                                          acc_pr=df['reg_date'],
    #                                          act_pr=df['act_unit'],
    #                                          price=df['price'],
    #                                          tax=df['tax'],
    #                                          subtotal=df['subtotal'],
    #                                          fees=df['fee'],
    #                                          total_price=df['total_price'],
    #                                          jeju_schedule_id=df['jeju_schedule_id'])
    # print(f'2 >>>> {reservation}')
    return JsonResponse(data=result, safe=False)

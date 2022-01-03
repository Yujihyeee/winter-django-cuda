from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, parser_classes
from price.models import Price
from price.models_process import Processing
from reservation.serializers import ReservationSerializer


@api_view(['GET'])
@parser_classes([JSONParser])
def pre_price(request):
    Processing().price_process()
    return JsonResponse({'PRICE': 'SUCCESS'})


@api_view(['POST'])
@parser_classes([JSONParser])
def get_price(request):
    # report = request.data
    # print(report)
    # arr = report[0]
    # dic = arr[0]
    print(request.data)
    dic = request.data
    plane_unit = {"plane_unit": Price.objects.filter(category_id__in=dic['plane'], category='plane').aggregate(Sum('price'))['price__sum']}
    people = {'people': dic['people']}
    plane_price = {'plane_price': plane_unit['plane_unit'] * people['people']}
    acc_unit = {'acc_unit': Price.objects.filter(category='accommodation', category_id=dic['acc_id']).values()[0]['price']}
    day = {'day': dic['day']}
    acc_price = {'acc_price': acc_unit['acc_unit'] * day['day']}
    act_unit = {'act_unit': Price.objects.filter(category_id__in=dic['activity'], category='activity').aggregate(Sum('price'))['price__sum']}
    act_price = {'act_price': act_unit['act_unit'] * people['people']}
    reg_date = {'reg_date': dic['reg_date']}
    date = {'reg_date': reg_date['reg_date'][:10]}
    price = {'price': plane_price['plane_price'] + acc_price['acc_price'] + act_price['act_price']}
    tax = {'tax': int(price['price'] * 0.1)}
    subtotal = {'subtotal': int(price['price'] + tax['tax'])}
    fees = {'fees': int(subtotal['subtotal'] * 0.2)}
    total_price = {'total_price': int(subtotal['subtotal'] + fees['fees'])}
    jeju_schedule = {'jeju_schedule': dic['id']}
    user = {'user': dic['user']}
    keys = []
    items = []
    for i in [date, people, day, plane_unit, acc_unit, act_unit, plane_price, acc_price, act_price, price, tax, subtotal, fees, total_price, jeju_schedule, user]:
        for j in i:
            keys.append(j)
            items.append(i[j])
    result = dict(zip(keys, items))
    serializer = ReservationSerializer(data=result, partial=True)
    # if serializer.is_valid():
    #     serializer.save()
    return JsonResponse(data=result, safe=False)

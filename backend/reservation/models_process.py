# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
from datetime import datetime
from django.db.models import Count, Sum
from price.models import Price, Pay
from reservation.models import Reservation
from common.models import ValueObject, Reader, Printer
from reservation.serializers import ReservationSerializer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'reservation/data/'
        vo.fname = 'price.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_reservation()

    def count(self):
        count_data = {}
        for i in range(6):
            today = datetime(year=2021, month=12, day=31).month
            count = Reservation.objects.filter(reg_date__month=today - i).aggregate(Count('id'))
            count_data[f'{i}번째'] = [f'{today - i}월', count['id__count']]
        count = count_data
        print(count)
        return count

    def insert_reservation(self):
        with open('', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                reservation = Reservation.objects.create(reg_date=row['reg_date'],
                                                         people=row['people'],
                                                         day=row['day'],
                                                         plane_pr=row['plane_pr'],
                                                         acc_pr=row['acc_pr'],
                                                         act_pr=row['act_pr'],
                                                         price=row['price'],
                                                         tax=row['tax'],
                                                         subtotal=row['subtotal'],
                                                         fees=row['fees'],
                                                         total_price=row['total_price'],
                                                         jeju_schedule=row['jeju_schedule'],
                                                         user=row['user'])
                print(f'2 >>>> {reservation}')
            print('DATA UPLOADED SUCCESSFULLY!')

    def year(self):
        result = [{f'plane{p}': Reservation.objects.filter(reg_date__month=p).aggregate(Sum('plane_price'))['plane_price__sum'],
                   f'acc{p}': Reservation.objects.filter(reg_date__month=p).aggregate(Sum('acc_price'))['acc_price__sum'],
                   f'activity{p}': Reservation.objects.filter(reg_date__month=p).aggregate(Sum('act_unit'))['act_unit__sum']} for p in range(1, 13)]
        return result

    def recent(self):
        data = Reservation.objects.order_by('-id')[:5].values()
        print(data)
        return data

    def dummy_sales(self):
        for i in Pay.objects.all():
            plane_unit = Price.objects.filter(category_id__in=i.plane, category='plane').aggregate(Sum('price'))['price__sum']
            acc_unit = Price.objects.filter(category_id=i.acc, category='accommodation').aggregate(Sum('price'))['price__sum']
            act_unit = Price.objects.filter(category_id__in=i.activity, category='activity').aggregate(Sum('price'))['price__sum']
            people = i.people
            day = i.day
            plane_price = plane_unit * people
            acc_price = acc_unit * day
            act_price = act_unit * people
            reg_date = i.reg_date
            price = plane_price + acc_price + act_price
            tax = int(price * 0.1)
            subtotal = int(price + tax)
            fees = int(subtotal * 0.2)
            total_price = int(subtotal + fees)
            jeju_schedule = i.re_id
            user = i.user
            a = Reservation.objects.create(reg_date=reg_date,
                                           people=people,
                                           day=day,
                                           plane_unit=plane_unit,
                                           plane_price=plane_price,
                                           acc_unit=acc_unit,
                                           acc_price=acc_price,
                                           act_unit=act_unit,
                                           act_price=act_price,
                                           price=price,
                                           tax=tax,
                                           subtotal=subtotal,
                                           fees=fees,
                                           total_price=total_price,
                                           jeju_schedule=jeju_schedule,
                                           user=user)
            print(f' 1 >>>> {a}')

    def insert_test(self):
        with open('reservation/data/dummy.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                a = Pay.objects.create(re_id=row['id'],
                                       reg_date=row['reg_date'],
                                       user=row['user'],
                                       day=row['day'],
                                       people=row['people'],
                                       plane=row['plane'],
                                       acc=row['acc'],
                                       activity=row['activity'])
                print(f' 1 >>>> {a}')
        print('Person DATA UPLOADED SUCCESSFULY!')

    def sum(self):
        total = Reservation.objects.all().aggregate(Sum('total_price'))
        print(total)
        return total

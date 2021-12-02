# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
from rest_framework.generics import get_object_or_404

from brevity.models import JejuSchedule
from reservation.models import Reservation
from jeju_data.models import Accommodation, Plane, Activity
from common.models import ValueObject, Reader, Printer


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

    def pre_process(self):
        arr = []
        for p in range(1, 12):
            pr = JejuSchedule.objects.get(pk=1)
            acc_pr = Accommodation.objects.get(pk=1)
            plane = Plane.objects.get(pk=1)
            activity = Activity.objects.get(pk=1)
            people = pr.people
            day = pr.day
            plane_pr = get_object_or_404(plane, id([]))
            activity = get_object_or_404(activity, id([]))
            reg_date = pr.startday - relativedelta(days=10)
            price = plane_pr + acc_pr.price + activity
            tax = (price * people) + (price * day) * 0.1
            subtotal = price + tax
            fee = subtotal * 0.2
            total_price = subtotal + fee
            print(p)
            arr.append(reg_date)
            arr.append(price)
            arr.append(int(tax))
            arr.append(int(subtotal))
            arr.append(int(fee))
            arr.append(int(total_price))
            print(arr)
        result = 0
        df = pd.DataFrame(result, columns=['reg_date', 'price', 'tax', 'subtotal', 'fees', 'total_price'])
        df.to_csv(self.csvfile + 'price.csv')

    def insert_reservation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                reservation = Reservation.objects.create(reg_date=row['reg_date'],
                                                         price=row['price'],
                                                         tax=row['tax'],
                                                         subtotal=row['subtotal'],
                                                         fees=row['fees'],
                                                         total_price=row['total_price'],
                                                         brevity_id=1)
                print(f'2 >>>> {reservation}')
            print('DATA UPLOADED SUCCESSFULLY!')

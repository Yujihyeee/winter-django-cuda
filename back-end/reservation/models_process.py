# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
import math
import pandas as pd
from jeju_schedule.models import JejuSchedule
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

    def pre_process(self, p):
        arr = []
        pr = JejuSchedule.objects.get(id=p)
        print(pr)
        plane = Plane.objects.filter(id__in=pr.plane).values('economyCharge')
        pl_df = pd.DataFrame(plane, columns=['economyCharge'])
        plane_pr = pl_df['economyCharge'].sum()
        acc_pr = Accommodation.objects.get(id=pr.acc_id)
        activity = Activity.objects.filter(id__in=pr.activity).values('price')
        act_df = pd.DataFrame(activity, columns=['price'])
        act_pr = act_df['price'].sum()
        people = pr.people
        day = pr.day
        unit = acc_pr.standard_number
        print(people/unit)
        acc_price = math.ceil(people/unit) * acc_pr.price * day
        print(acc_price)
        reg_date = pr.reg_date.date()
        price = (plane_pr * people) + acc_price + act_pr
        tax = price * 0.1
        subtotal = price + tax
        fee = subtotal * 0.2
        total_price = subtotal + fee
        jeju_schedule_id = p
        arr.append(reg_date)
        arr.append(people)
        arr.append(day)
        arr.append(plane_pr)
        arr.append(acc_pr.price)
        arr.append(act_pr)
        arr.append(price)
        arr.append(int(tax))
        arr.append(int(subtotal))
        arr.append(int(fee))
        arr.append(int(total_price))
        arr.append(jeju_schedule_id)
        n = 12
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['reg_date', 'people', 'day', 'plane_pr', 'acc_pr', 'act_pr', 'price', 'tax',
                                           'subtotal', 'fees', 'total_price', 'jeju_schedule_id'])
        df.to_csv(self.csvfile)

    def insert_reservation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
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
                                                         jeju_schedule_id=row['jeju_schedule_id'])
                print(f'2 >>>> {reservation}')
            print('DATA UPLOADED SUCCESSFULLY!')

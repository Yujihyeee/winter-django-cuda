# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv

import pandas as pd
from django.db.models import Sum
import brevity
from brevity.models import JejuSchedule
from reservation.models import Reservation
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
        price = 0
        people = 0
        day = 0
        tax = (price * people) + (price * day) * 0.1
        subtotal = price + tax
        fee = subtotal * 0.2
        total_price = subtotal + fee


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

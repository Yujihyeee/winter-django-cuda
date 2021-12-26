import csv

import pandas as pd

from common.models import ValueObject, Reader, Printer
from jeju_data.models import Plane, Accommodation, Activity
from price.models import Price


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'price/data/'
        vo.fname = 'price.csv'
        self.csvfile = reader.new_file(vo)

    def price_process(self):
        arr = []
        for i in range(1, 278):
            with open('price/data/plane.csv', newline='', encoding='utf8') as f:
                data_reader = csv.DictReader(f)
                for row in data_reader:
                    reservation = Price.objects.create(id=row['id'],
                                                       category_id=row['id'],
                                                       price=row['price']
                                                       )
                    print(f'2 >>>> {reservation}')
            plane = Plane.objects.get(pk=i)
            plane_id = plane.id
            plane_pr = plane.economyCharge
            print(plane_id, plane_pr)
            arr.append(plane_id)
            arr.append(plane_pr)

        for i in range(1, 20):
            with open('price/data/accommodation.csv', newline='', encoding='utf8') as f:
                data_reader = csv.DictReader(f)
                for row in data_reader:
                    reservation = Price.objects.create(id=row['id'],
                                                       category_id=row['id'],
                                                       price=row['price']
                                                       )
                    print(f'2 >>>> {reservation}')
            acc = Accommodation.objects.get(pk=i)
            acc_id = acc.id
            acc_pr = acc.price
            print(acc_id, acc_pr)
            arr.append(acc_id)
            arr.append(acc_pr)

        for i in range(1, 32):
            with open('price/data/activity.csv', newline='', encoding='utf8') as f:
                data_reader = csv.DictReader(f)
                for row in data_reader:
                    reservation = Price.objects.create(id=row['id'],
                                                       category_id=row['id'],
                                                       price=row['price']
                                                       )
                    print(f'2 >>>> {reservation}')
            act = Activity.objects.get(pk=i)
            act_id = act.id
            act_pr = act.price
            print(act_id, act_pr)

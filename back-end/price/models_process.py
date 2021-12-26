import csv

import pandas as pd

import price
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
        with open('price/data/plane.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['vihicleId'],
                                             category='plane',
                                             price=row['economyCharge']
                                             )
                print(f'2 >>>> {price}')

        with open('price/data/accommodation.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['name'],
                                             category='accommodation',
                                             price=row['1박당가격']
                                             )
                print(f'2 >>>> {price}')

        with open('price/data/activity.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['name'],
                                             category='activity',
                                             price=row['expense']
                                             )
                print(f'2 >>>> {price}')

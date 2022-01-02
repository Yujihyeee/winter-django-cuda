import csv
import random

import pandas as pd
from common.models import ValueObject, Reader, Printer
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

    def count_random(self):
        arr = []

        def count():
            return random.randint(50, 100)

        def year():
            for i in range(2001, 2022):
                return f'{i}'

        def month():
            for month in range(1, 13):
                if month < 10:
                    month = f'0{month}'
                else:
                    continue
            return month

        def date():
            return f'{year()}-{month()}'

        for i in range(146):
            arr.append(date())
            arr.append(count())
        n = 2
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'count'])
        print(df)
        # df.to_csv('ledger/data/cost.csv')

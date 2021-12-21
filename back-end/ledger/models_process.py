# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
import datetime
import random

import pandas as pd
from ledger.models import Ledger
from common.models import ValueObject, Reader, Printer
from reservation.models import Reservation


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'ledger/data/'
        vo.fname = 'test.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_ledger()

    def pre_process(self):
        arr = []
        for t in range(1, 5):
            t = Reservation.objects.get(pk=t)
            total = t.total_price
            price = t.price
            date = t.reg_date
            arr.append(date)
            arr.append('매출액')
            arr.append(total)
            arr.append(date)
            arr.append('매출원가')
            arr.append(price)
        n = 3
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'category', 'price'])
        print(df)
        df.to_csv(self.csvfile)

    def insert_cost(self):
        arr = []

        def create_price():
            return random.randint(10000, 1000000)

        def create_month():
            month = random.randint(1, 12)
            if month < 10:
                month = f'0{month}'
            return month

        def create_day():
            day = random.randint(1, 28)
            if day < 10:
                day = f'0{day}'
            return day

        def create_date():
            return f'2021-{create_month()}-{create_day()}'

        for i in range(1000):
            arr.append(create_date())
            arr.append('판매비와관리비')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('지급수수료')
            arr.append(create_price())
            arr.append(create_date())
            arr.append('금융비용')
            arr.append(create_price())
        n = 3
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['date', 'category', 'price'])
        print(df)
        df.to_csv('ledger/data/cost.csv')

    def insert_ledger(self):
        with open('ledger/data/cost.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ledger = Ledger.objects.create(date=row['date'],
                                               category=row['category'],
                                               price=row['price'])
                print(f'2 >>>> {ledger}')
            print('DATA UPLOADED SUCCESSFULLY!')

# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv

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
        for t in range(1, 19):
            t = Reservation.objects.get(pk=t)
            total = t.total_price
            price = t.price
            date = t.reg_date
            print(date, total)
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
        df.to_csv(self.csvfile + 'test.csv')

    def insert_ledger(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ledger = Ledger.objects.create(date=row['date'],
                                               category='매출액',
                                               price=row['price_id'])
                print(f'2 >>>> {ledger}')
            print('DATA UPLOADED SUCCESSFULLY!')

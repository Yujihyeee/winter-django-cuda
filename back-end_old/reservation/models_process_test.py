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
        arr = []
        for p in range(1, 31):
            # print(f' 유저아이디: {p}')
            pr = JejuSchedule.objects.get(pk=p)
            price = pr.plane + pr.accommodation + pr.activity
            tax = price * 0.1
            subtotal = price + tax
            fees = subtotal * 0.2
            total_price = subtotal + fees
            # print(price, int(tax), int(subtotal), int(fees), int(total_price))
            arr.append(price)
            arr.append(int(tax))
            arr.append(int(subtotal))
            arr.append(int(fees))
            arr.append(int(total_price))
            # print(arr)
        n = 5
        result = [arr[i * n:(i + 1) * n] for i in range((len(arr) + n - 1) // n)]
        df = pd.DataFrame(result, columns=['price', 'tax', 'subtotal', 'fees', 'total_price'])
        df.to_csv(self.csvfile + 'price.csv')

    def insert_reservation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                reservation = Reservation.objects.create(price=row['price'],
                                                         tax=row['tax'],
                                                         subtotal=row['subtotal'],
                                                         fees=row['fees'],
                                                         total_price=row['total_price'],
                                                         brevity_id=1)
                print(f'2 >>>> {reservation}')
            print('DATA UPLOADED SUCCESSFULLY!')

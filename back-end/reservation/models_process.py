# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
from django.db.models import Sum
import brevity
from brevity.models import Brevity
from reservation.models import Reservation
from common.models import ValueObject, Reader, Printer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'brevity/data/'
        vo.fname = 'brevity_dummy_2.csv'
        self.csvfile = reader.new_file(vo)

    def pre_process(self):
        arr = []
        for p in range(1, 31):
            print(f' 유저아이디: {p}')
            pr = Brevity.objects.get(pk=p)
            price = pr.plane + pr.accommodation + pr.activity
            tax = price * 0.1
            subtotal = price + tax
            fees = subtotal * 0.2
            total_price = subtotal + fees
            print(price, int(tax), int(subtotal), int(fees), int(total_price))
            arr.append(int(total_price))
        return arr

    def insert_reservation(self, arr):
        data_reader = arr
        for row in data_reader:
            reservation = Reservation.objects.create(userid=row['id'],
                                                     price=row['price'],
                                                     tax=row['tax'],
                                                     subtotal=row['subtotal'],
                                                     fees=row['fees'],
                                                     total_price=row['total_price']
                                                     )
            print(f'2 >>>> {reservation}')
        print('DATA UPLOADED SUCCESSFULLY!')

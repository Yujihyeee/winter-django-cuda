# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
from django.db.models import Sum
from brevity.models import Brevity
from common.models import ValueObject, Reader, Printer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'brevity/data/'
        vo.fname = 'brevity_dummy_2.csv'
        self.csvfile = reader.new_file(vo)

    def process(self):
        # price = Brevity.objects.filter(columns=['plane', 'accommodation', 'activity']).aggregate(Sum())
        price = Brevity.objects.all().aggregate(Sum(['plane', 'accommodation', 'activity']))
        tax = price * 0.1
        subtotal = price + tax
        fees = subtotal * 0.2
        total_price = subtotal + fees
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not Brevity.objects.filter(category=row['항목명']).exists():
                reservation = Brevity.objects.create(tax=row['tax'],
                                                     subtotal=row['subtotal'],
                                                     fees=row['fees'],
                                                     total_price=row['total_price'],
                                                     price=row['price'])
                print(f'2 >>>> {reservation}')
        print('DATA UPLOADED SUCCESSFULLY!')

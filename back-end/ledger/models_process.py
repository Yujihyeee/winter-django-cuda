# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
import csv
from ledger.models import Ledger
from common.models import ValueObject, Reader, Printer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'ledger/data/'
        vo.fname = ''
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_ledger()

    def pre_process(self):
        pass

    def insert_ledger(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ledger = Ledger.objects.create(reg_date=row['reg_date'],
                                               price=row['price'],
                                               jeju_schedule_id=row['jeju_schedule_id'])
                print(f'2 >>>> {ledger}')
            print('DATA UPLOADED SUCCESSFULLY!')

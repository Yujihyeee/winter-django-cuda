import os
import django
import csv
import sys
from icecream import ic
from common.models import ValueObject, Printer, Reader
# system setup
# SET FOREIGN_KEY_CHECKS = 0;
from fin_reports.models import FinReports


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'fin_reports/data/'
        vo.fname='2020_PL.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_fin_report()

    def insert_fin_report(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)

            for row in data_reader:
                if not FinReports.objects.filter(year=row['결산기준일']).exists():
                    fin_reports = FinReports.objects.create(year=row['결산기준일'],
                                                            category=row['항목명'],
                                                            price=row['당기'])
                    print(f'1 >>>> {fin_reports}')
        print('USER DATA UPLOADED SUCCESSFULY!')

import os
import django
import csv
import sys

import pandas as pd
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
        vo.fname='2020_PL.2.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_fin_report()

    def insert_fin_report(self):
        df = pd.read_csv(self.csvfile, encoding='UTF-8', thousands=',')
        df = df.fillna(0)
        df.to_csv(self.csvfile + '2020_PL.csv')
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not FinReports.objects.filter(category=row['항목명']).exists():
                fin_reports = FinReports.objects.create(year=2018,
                                                        category=row['항목명'],
                                                        price=int(float(row['전전기'])))
                print(f'1 >>>> {fin_reports}')
        print('USER DATA UPLOADED SUCCESSFULY!')

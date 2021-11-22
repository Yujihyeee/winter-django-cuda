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
        vo.fname='2020_PL_2.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_fin_report()

    def insert_fin_report(self):
        # # price['당기'] = price['당기'].fillna(0)
        # # print(price.isnull().sum())
        # df = pd.read_csv(self.csvfile, encoding='UTF-8', thousands=',')
        # #  df['crime'] = df['살인 발생'] + df['강도 발생'] + df['강간 발생'] + df['절도 발생'] + df['폭력 발생']
        # #  df['arrest'] = df.groupby(df['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'])
        # df.to_csv(self.csvfile + '2020_PL_2.csv')
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                if not FinReports.objects.filter(category=row['항목명']).exists():
                    fin_reports = FinReports.objects.create(year=2020,
                                                            category=row['항목명'],
                                                            price=row['당기'])
                    print(f'1 >>>> {fin_reports}')
        #             row['결산기준일']
        print('USER DATA UPLOADED SUCCESSFULY!')

import csv
import pandas as pd
from common.models import ValueObject, Printer, Reader
from brevity.models import Brevity


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'brevity/data/'
        vo.fname = 'brevity_dummy_2.csv'
        self.csvfile = reader.new_file(vo)

    # def insert_data(self):
    #     self.insert_brevity()

    def pre_process(self):
        df = pd.read_csv(self.csvfile, encoding='UTF-8', thousands=',')
        colstocheck = df.columns
        df[colstocheck] = df[colstocheck].replace({'\¥': ''}, regex=True)
        df[colstocheck] = df[colstocheck].replace({'\.': ''}, regex=True)
        df.to_csv(self.csvfile + 'brevity_dummy_2.csv')

    def insert_brevity(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not brevity.objects.filter(category=row['항목명']).exists():
                brevity = Brevity.objects.create(userid=row['userid'],
                                                 plane=row['plane'],
                                                 accommodation=row['accommodation'],
                                                 activity=row['activity'])
                print(f'2 >>>> {brevity}')
        print('DATA UPLOADED SUCCESSFULLY!')

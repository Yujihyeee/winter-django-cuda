import csv
import pandas as pd
from common.models import ValueObject, Printer, Reader
from brevity.models import JejuSchedule


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'brevity/data/'
        vo.fname = 'dum.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_brevity()

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
                jeju_schedule = JejuSchedule.objects.create(startday=row['startday'],
                                                            endday=row['endday'],
                                                            day=row['day'],
                                                            startloc=row['startloc'],
                                                            people=row['people'],
                                                            relationship=row['relationship'],
                                                            plane=row['plane'],
                                                            activity=row['activity'],
                                                            olle=row['olle'],
                                                            restaurant=row['restaurant'],
                                                            tourism=row['tourism'],
                                                            shop=row['shop'],
                                                            schedule=row['schedule'],
                                                            acc_id=row['acc_id'],
                                                            category_id=row['category_id'],
                                                            user_id=row['user_id'])
                print(f'2 >>>> {jeju_schedule}')
        print('DATA UPLOADED SUCCESSFULLY!')

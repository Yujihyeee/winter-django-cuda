import csv
from common.models import ValueObject, Printer, Reader
from jeju_schedule.models import JejuSchedule


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'jeju_schedule/data/'
        vo.fname = 'dum.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_schedule()

    def insert_schedule(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                # if not JejuSchedule.objects.filter(schedule=row['schedule']).exists():
                jeju_schedule = JejuSchedule.objects.create(reg_date=row['reg_date'],
                                                            startday=row['startday'],
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

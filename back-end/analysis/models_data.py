import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
import django
django.setup()
import csv
from icecream import ic
from analysis.models import VisitorNumber
from common.models import ValueObject, Reader, Printer


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'analysis/data/'
        vo.fname = 'visitor_with.csv'
        self.csvfile = reader.new_file(vo)

    def insert_visitor(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                if not VisitorNumber.objects.filter(month=f"{row['year']}-01").exists():
                    v = VisitorNumber.objects.create(month=f"{row['year']}-01",
                                                     local=row['korea'],
                                                     foreigner=row['foreigner'])
                    print(f'data >>>>>>>>> {v}')
        print('VisitorNumber DATA UPLOADED SUCCESSFULY!')

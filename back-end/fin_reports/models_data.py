import os
import django
import csv
import sys
from common.models import ValueObject, Printer, Reader
# system setup

# SET FOREIGN_KEY_CHECKS = 0;


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'product/data/'
        vo.fname='product.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        self.insert_vendor()
        self.insert_category()
        self.insert_product()

    def insert_vendor(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                if not Vendor.objects.filter(name=row['vendor']).exists():
                    vendor = Vendor.objects.create(name=row['vendor'])
        print('VENDOR DATA UPLOADED SUCCESSFULY!')

    def insert_category(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                if not Category.objects.filter(name=row['category']).exists():
                    category = Category.objects.create(name=row['category'])
        print('CATEGORY DATA UPLOADED SUCCESSFULY!')

    def insert_product(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                v = Vendor()
                vendor = Vendor.objects.all().filter(name=row['vendor']).values()[0]
                v.id = vendor['id']
                c = Category()
                category = Category.objects.all().filter(name=row['category']).values()[0]
                c.id = category['id']
                Product.objects.create(name=row['product'] ,
                                       price=row['price'],
                                       category=c,
                                       vendor=v)
            print('PRODUCT DATA UPLOADED SUCCESSFULY!')

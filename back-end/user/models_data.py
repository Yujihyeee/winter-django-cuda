import os
from datetime import datetime
import django
import csv
import sys
from common.models import ValueObject, Reader, Printer
from user.models import Person, User

# system setup
#
# SET FOREIGN_KEY_CHECKS = 0;

from image.models import Category, Image
from icecream import ic
# import datetime

from sphinx.util import requests
import json


class DbUploader():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'user/data/'
        # vo.fname = 'persons.csv'
        vo.fname = 'user.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        print('############ 2 ##########')
        # self.insert_category_person()
        print('############ 3 ##########')
        # self.insert_table_user()
        print('############ 4 ##########')
        # self.insert_planes()
        print('############ 5 ##########')
        # self.insert_jeju()
        print('############ ok ##########')

    def insert_category_person(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='person').values()[0]
                c.id = category['id']

                # if row['gender'] == '여':
                #     True
                # if not row['gender'] == '여':
                #     False

                # if not Person.objects.filter(type=row['category']).exists():  # 동일한 값 있으면 넘어가
                a = Person.objects.create(age=row['age'],
                                          # gender=row['gender'],
                                          gender= True if row['gender'] == 'woman' else False,
                                          mbti=row['mbti'],
                                          category=c)
                print(f' 1 >>>> {a}')
        print('Tourism DATA UPLOADED SUCCESSFULY!')

    def insert_table_user(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='user').values()[0]
                c.id = category['id']

                cp = Person()
                today = datetime.now()
                brith = datetime.strptime(row['birth'], '%Y-%m-%d')
                age = today.year-brith.year
                age = f'{str(int(age/10))}0'
                # print(age)
                categoryP = Person.objects.all().filter(mbti=row['mbti'],
                                                       gender=True if row['gender'] == '여' else False,
                                                       age=age).values()[0]
                cp.id = categoryP['id']
                i = Image()
                image = Image.objects.all().filter(name=row['gender']).values()[0]
                i.id = image['id']
                # if Tourism.objects.filter(address=row['address']).exists():  # 동일한 값 있으면
                #     geo = self.trans_geo(db['address'])
                #     print(geo)
                #     if geo != 0:
                #         tourism = Tourism.objects.filter(address=row['address']).update(lat=geo['lat'], log=geo['long'])
                #         print(f' 1 >>>> {tourism}')
                if not User.objects.filter(name=row['name']).exists():  # 동일한 값 있으면 넘어가
                    # geo = self.trans_geo(row['address'])
                    # print(geo)
                    # if geo != 0:
                        user = User.objects.create(username=row['username'],
                                                   password=row['password'],
                                                   name=row['name'],
                                                   email=row['email'],
                                                   birth=row['birth'],
                                                   gender=row['gender'],
                                                   mbti=row['mbti'],
                                                   mbti_list=row['mbti_list'],
                                                   card_number=row['card_number'],
                                                   card_company=row['card_company'],
                                                   person_category=cp,
                                                   category=c,
                                                   image=i,)
                        print(f' 1 >>>> {user}')
        print('User DATA UPLOADED SUCCESSFULY!')

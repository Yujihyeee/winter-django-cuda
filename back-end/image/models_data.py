import os
import django
import csv
import sys
import pandas as pd
from icecream import ic
from common.models import ValueObject, Reader, Printer
# system setup
from image.models import Image, Category


class DbUploader():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        # vo.context = 'image/data/'
        # vo.fname = 'category.csv'
        # vo.context = 'jeju_data/data/'
        # vo.fname = 'jejuolle.csv'
        vo.context = 'user/data/'
        vo.fname = 'user.csv'
        # restaurant, shop, tourism, activity, plane, accommodation, jejuolle
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        print('############ 2 ##########')
        # self.image_category()
        print('############ 3 ##########')
        # self.insert_image()
        print('############ 4 ##########')
        # self.insert_planes()
        print('############ 5 ##########')
        # self.insert_jeju()
        print('############ ok ##########')

    def image_category(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                if not Category.objects.filter(category=row['category']).exists():  # 동일한 값 있으면 넘어가
                    category = Category.objects.create(section=row['section'],
                                                       category=row['category'])
                    print(f' 1 >>>> {category}')
        print('Tourism DATA UPLOADED SUCCESSFULY!')

    def test(self):
        df = pd.read_csv(self.csvfile, encoding='utf-8')
        print(df)

    def insert_image(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='olle').values()[0]
                c.id = category['id']
                if not Image.objects.filter(name=row['course-name']).exists():  # 동일한 값 있으면 넘어가
                        image = Image.objects.create(category=c,
                # Image.objects.create(category=c,
                                                     name=row['course-name'],
                                                     url=f"{row['illustration']},{row['map']},{row['vmap']}"
                                                     # url=row['url'],
                                                     # url_3=row['vmap']
                                                     )
                        print(f' 1 >>>> {image}')
        print('IMAGE DATA UPLOADED SUCCESSFULY!')

    # def insert_planes(self):
    #     with open(self.csvfile, newline='', encoding='utf8') as f:
    #         data_reader = csv.DictReader(f)
    #         for row in data_reader:
    #             if not Plane.objects.filter(vihicleId=row['vihicleId']).exists():
    #                 plane = Plane.objects.create(vihicleId=row['vihicleId'],
    #                                              airlineNm=row['airlineNm'],
    #                                              depPlandTime=row['depPlandTime'],
    #                                              arrPlandTime=row['arrPlandTime'],
    #                                              economyCharge=row['economyCharge'],
    #                                              depAirportNm=row['depAirportNm'],
    #                                              arrAirportNm=row['arrAirportNm'])
    #                 print(f' 1 >>>> {plane}')
    #     print('Plane DATA UPLOADED SUCCESSFULY!')

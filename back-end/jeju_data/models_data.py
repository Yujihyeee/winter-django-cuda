import os
import django
import csv
import sys
from common.models import ValueObject, Reader, Printer
# system setup
# SET FOREIGN_KEY_CHECKS = 0;
from image.models import Category, Image
from jeju_data.models import Tourism, Activity, Plane, TourismCategory, ActivityCategory, Shop, PlaneCategory, \
    RestaurantCategory, Restaurant, AccommodationCategory, Accommodation, Olle
from icecream import ic
from sphinx.util import requests
import json


class DbUploader:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'jeju_data/data/'
        vo.fname = 'tourism.csv'
        # vo.fname = 'activity.csv'
        # vo.fname = 'plane.csv'
        # vo.fname = 'restaurant.csv'
        # vo.fname = 'accommodation.csv'
        # vo.fname = 'jejuolle.csv'
        # vo.fname = 'shop.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        print('############ 2 ##########')
        self.insert_category_tourism()
        # self.insert_category_activity()
        # self.insert_category_plane()
        # self.insert_category_restaurant()
        # self.insert_category_accommodation()
        print('############ 3 ##########')
        self.insert_table_tourism()
        # self.insert_table_activity()
        # self.insert_table_plane()
        # self.insert_table_restaurant()
        # self.insert_table_accommodation()
        # self.insert_table_olle()
        # self.insert_table_shop()
        print('############ 4 ##########')
        # self.insert_planes()
        print('############ 5 ##########')
        # self.insert_jeju()
        print('############ ok ##########')

    def insert_category_tourism(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='tourism').values()[0]
                c.id = category['id']
                if not TourismCategory.objects.filter(type=row['category']).exists():  # 동일한 값 있으면 넘어가
                    a = TourismCategory.objects.create(type=row['category'],
                                                       category=c)
                    print(f' 1 >>>> {a}')
        print('Tourism DATA UPLOADED SUCCESSFULLY!')

    def insert_table_tourism(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = TourismCategory()
                category = TourismCategory.objects.filter(type=row['category']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.filter(name=row['name']).values()[0]
                print(image)
                i.id = image['id']

                if not Tourism.objects.filter(name=row['name']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.trans_geo(row['address'])
                    print(geo)
                    if geo != 0:
                        tourism = Tourism.objects.create(name=row['name'],
                                                         address=row['address'],
                                                         explanation=row['explanation'],
                                                         lat=geo['lat'],
                                                         log=geo['long'],
                                                         tour_category=c,
                                                         image=i)
                        print(f' 1 >>>> {tourism}')
        print('Tourism DATA UPLOADED SUCCESSFULLY!')

    def insert_category_activity(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='activity').values()[0]
                c.id = category['id']
                if not ActivityCategory.objects.filter(type=row['category']).exists():  # 동일한 값 있으면 넘어가
                    a = ActivityCategory.objects.create(type=row['category'],
                                                        section=c,
                                                        category=row['section'])
                    print(f' 1 >>>> {a}')
        print('ActivityCategory DATA UPLOADED SUCCESSFULLY!')

    def insert_table_activity(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = ActivityCategory()
                category = ActivityCategory.objects.all().filter(type=row['category']).values()[0]
                # print(category)
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']

                if not Activity.objects.filter(name=row['name']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.trans_geo(row['location'])
                    if geo != 0:
                        activity = Activity.objects.create(name=row['name'],
                                                           start_business_time=row['start time'],
                                                           end_business_time=row['end time'],
                                                           time=row['time'],
                                                           contact=row['contact'],
                                                           loc=row['location'],
                                                           price=row['expense'],
                                                           lat=geo['lat'],
                                                           log=geo['long'],
                                                           act_category=c,
                                                           image=i,)
                        print(f' 1 >>>> {activity}')
        print('Activity DATA UPLOADED SUCCESSFULLY!')

    def insert_table_shop(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='shop').values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']

                if not Shop.objects.filter(name=row['name']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.trans_geo(row['loc'])
                    if geo != 0:
                        shop = Shop.objects.create(name=row['name'],
                                                   loc=row['loc'],
                                                   lat=geo['lat'],
                                                   log=geo['long'],
                                                   explanation=row['explanation'],
                                                   recommend=row['category'],
                                                   category=c,
                                                   image=i,)
                        print(f' 1 >>>> {shop}')
        print('Shop DATA UPLOADED SUCCESSFULLY!')

    def insert_category_plane(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='plane').values()[0]
                c.id = category['id']
                if not PlaneCategory.objects.filter(type=row['depAirportNm']+"-"+row['arrAirportNm']).exists():  # 동일한 값 있으면 넘어가
                    a = PlaneCategory.objects.create(type=row['depAirportNm']+"-"+row['arrAirportNm'],
                                                              section=c,
                                                              category=row['type'])
                    print(f' 1 >>>> {a}')
        print('PlaneCategory DATA UPLOADED SUCCESSFULLY!')

    def insert_table_plane(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = PlaneCategory()
                category = PlaneCategory.objects.all().filter(type=row['depAirportNm']+"-"+row['arrAirportNm']).values()[0]
                c.id = category['id']
                if not Plane.objects.filter(vihicleId=row['vihicleId']).exists():
                    plane = Plane.objects.create(vihicleId=row['vihicleId'],
                                                 airlineNm=row['airlineNm'],
                                                 economyCharge=row['economyCharge'],
                                                 depPlandTime=row['depPlandTime'],
                                                 arrPlandTime=row['arrPlandTime'],
                                                 plane_category=c)
                    print(f' 1 >>>> {plane}')
        print('Plane DATA UPLOADED SUCCESSFULLY!')

    def insert_category_restaurant(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='restaurant').values()[0]
                c.id = category['id']
                if not RestaurantCategory.objects.filter(type=row['category']).exists():  # 동일한 값 있으면 넘어가
                    a = RestaurantCategory.objects.create(type=row['category'],
                                                          category=c)
                    print(f' 1 >>>> {a}')
        print('RestaurantCategory DATA UPLOADED SUCCESSFULLY!')

    def insert_table_restaurant(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = RestaurantCategory()
                category = RestaurantCategory.objects.all().filter(type=row['category']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']

                if not Restaurant.objects.filter(name=row['name']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.trans_geo(row['address'])
                    if geo != 0:
                        restaurant = Restaurant.objects.create(name=row['name'],
                                                               loc=row['address'],
                                                               recommend=row['food'],
                                                               res_category=c,
                                                               lat=geo['lat'],
                                                               log=geo['long'],
                                                               image=i,)
                        print(f' 1 >>>> {restaurant}')
        print('Restaurant DATA UPLOADED SUCCESSFULLY!')

    def insert_category_accommodation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                ic(row)
                c = Category()
                category = Category.objects.all().filter(category='accommodation').values()[0]
                c.id = category['id']
                if not AccommodationCategory.objects.filter(type=row['구분']).exists():  # 동일한 값 있으면 넘어가
                    a = AccommodationCategory.objects.create(type=row['구분'],
                                                             category=c)
                    print(f' 1 >>>> {a}')
        print('AccommodationCategory DATA UPLOADED SUCCESSFULLY!')

    def insert_table_accommodation(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = AccommodationCategory()
                category = AccommodationCategory.objects.all().filter(type=row['구분']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['상호명']).values()[0]
                i.id = image['id']

                if not Accommodation.objects.filter(name=row['상호명']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.trans_geo(row['소재지'])
                    if geo != 0:
                        accommodation = Accommodation.objects.create(name=row['상호명'],
                                                                     loc=row['소재지'],
                                                                     price=row['1박당가격'],
                                                                     contact=row['연락처'],
                                                                     standard_number=row['숙박인원'],
                                                                     lat=geo['lat'],
                                                                     log=geo['long'],
                                                                     acc_category=c,
                                                                     image=i,)
                        print(f' 1 >>>> {accommodation}')
        print('Accommodation DATA UPLOADED SUCCESSFULLY!')

    def insert_table_olle(self):
        with open(self.csvfile, newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='olle').values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['course-name']).values()[0]
                i.id = image['id']

                if not Olle.objects.filter(name=row['course-name']).exists():  # 동일한 값 있으면 넘어가
                    geo = self.getAddress(row['starting-point'])
                    if geo != 0:
                        olle = Olle.objects.create(course=row['course'],
                                                   name=row['course-name'],
                                                   distance=row['distance(km)'],
                                                   time=row['time'],
                                                   starting_point=row['starting-point'],
                                                   end_point=row['end-point'],
                                                   lat=geo['lat'],
                                                   log=geo['long'],
                                                   explanation=row['explanation'],
                                                   category=c,
                                                   image=i)
                        print(f' 1 >>>> {olle}')
        print('Olle DATA UPLOADED SUCCESSFULLY!')

    def trans_geo(self, addr):
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr
        headers = {"Authorization": "KakaoAK 494e0b25b56b815a43298d2314a551a0"}
        result = json.loads(str(requests.get(url, headers=headers).text))
        status_code = requests.get(url, headers=headers).status_code
        if (status_code != 200):
            return 0

        try:
            match_first = result['documents'][0]['address']
            long = match_first['x']
            lat = match_first['y']

            return {'long': long, 'lat': lat}
        except IndexError:  # match값이 없을때
            return 0
        except TypeError:  # match값이 2개이상일때
            return 0

    def getAddress(self, keyword):
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + keyword
        headers = {"Authorization": "KakaoAK 851f4e6cf0cce36ebf456a4eb33b94d4"}
        # get 방식으로 주소를 포함한 링크를 헤더와 넘기면 result에 json형식의 주소와 위도경도 내용들이 출력된다.
        result = json.loads(str(requests.get(url, headers=headers).text))
        status_code = requests.get(url, headers=headers).status_code
        if (status_code != 200):
            # print(f"ERROR: Unable to call rest api, http_status_coe: {status_code}")
            return 0
        try:
            match_first = result['documents'][0]
            long = match_first['x']
            lat = match_first['y']
            address = match_first['road_address_name']
            # print(x)
            # print(y)
            # print(address)
            return {'long': long, 'lat': lat}
        except IndexError:  # match값이 없을때
            print('match값이 없을때')
            # x, y, address = '0', '0', '0'
            return 0
        except TypeError:  # match값이 2개이상일때
            print('match값이 2개이상일때')
            x, y, address = '1', '1', '1'
            # return x, y, address
            return 0

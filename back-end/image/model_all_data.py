import os
from jeju_data.models import TourismCategory, Tourism, ActivityCategory, Activity, PlaneCategory, Plane, \
    RestaurantCategory, Restaurant, AccommodationCategory, Accommodation, Olle, Shop
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
import django
django.setup()
import csv
from sphinx.util import requests
import json
from image.models import Category, Image
from user.models import Person


class AllDbUploader:
    def insert_db_data(self):
        print('################ 1 init ################')
        category_csv = 'image/data/category.csv'
        restaurant_csv = 'jeju_data/data/restaurant.csv'
        shop_csv = 'jeju_data/data/shop.csv'
        tourism_csv = 'jeju_data/data/tourism.csv'
        activity_csv = 'jeju_data/data/activity.csv'
        plane_csv = 'jeju_data/data/plane.csv'
        accommodation_csv = 'jeju_data/data/accommodation.csv'
        jejuolle_csv = 'jeju_data/data/jejuolle.csv'
        persons_csv = 'user/data/persons.csv'
        user_csv = 'user/data/user.csv'
        print('################ 2 category ################')
        self.insert_category(category_csv)
        print('################ 3 image ################')
        self.insert_image_url(restaurant_csv, 'restaurant', 'name')
        self.insert_image_url(tourism_csv, 'tourism', 'name')
        self.insert_image_url(activity_csv, 'activity', 'name')
        self.insert_image_url(shop_csv, 'shop', 'name')
        self.insert_image_url(accommodation_csv, 'accommodation', 'name')
        self.insert_image_olle_url(jejuolle_csv, 'olle', 'course-name')
        self.insert_image_url(user_csv, 'user', 'gender')
        print('################  4 jeju_category_data  ################')
        self.insert_category_tourism(tourism_csv)
        self.insert_category_activity(activity_csv)
        self.insert_category_plane(plane_csv)
        self.insert_category_restaurant(restaurant_csv)
        self.insert_category_accommodation(accommodation_csv)
        print('################  5 jeju_data  ################')
        self.insert_table_tourism(tourism_csv)
        self.insert_table_activity(activity_csv)
        self.insert_table_plane(plane_csv)
        self.insert_table_restaurant(restaurant_csv)
        self.insert_table_accommodation(accommodation_csv)
        self.insert_table_olle(jejuolle_csv)
        self.insert_table_shop(shop_csv)
        print('################ 6 person ################')
        self.insert_category_person(persons_csv)
        print('################ 끝   끝   끝 ################')

    def insert_category(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                if not Category.objects.filter(category=row['category']).exists():
                    category = Category.objects.create(section=row['section'],
                                                       category=row['category'])
                    print(f' Category >>>> {category}')
        print('Category DATA UPLOADED SUCCESSFULY!')

    def insert_image_url(self, csvt, category_type, name):
        with open(f'{csvt}', newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category= f'{category_type}').values()[0]
                c.id = category['id']
                if not Image.objects.filter(name=row[name]).exists():
                        image = Image.objects.create(category=c,
                                                     name=row[name],
                                                     url=row['url']
                                                     )
                        print(f' IMAGE >>>> {image}')
        print('IMAGE DATA UPLOADED SUCCESSFULY!')

    def insert_image_olle_url(self, csvt, category_type, name):
        with open(f'{csvt}', newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category=f'{category_type}').values()[0]
                c.id = category['id']
                if not Image.objects.filter(name=row[name]).exists():
                        image = Image.objects.create(category=c,
                                                     name=row[name],
                                                     url=f"{row['illustration']},{row['map']},{row['vmap']}"
                                                     )
                        print(f' IMAGE OLLE DATA >>>> {image}')
        print('IMAGE OLLE DATA UPLOADED SUCCESSFULY!')

    def insert_category_person(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='person').values()[0]
                c.id = category['id']
                a = Person.objects.create(age=row['age'],
                                          gender=True if row['gender'] == 'woman' else False,
                                          mbti=row['mbti'],
                                          category=c)
                print(f' PERSON DATA >>>> {a}')
        print('PERSON DATA UPLOADED SUCCESSFULY!')

    def insert_category_tourism(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='tourism').values()[0]
                c.id = category['id']
                if not TourismCategory.objects.filter(type=row['category']).exists():
                    a = TourismCategory.objects.create(type=row['category'],
                                                       category=c)
                    print(f' Tourism Category >>>> {a}')
        print('Tourism Category DATA UPLOADED SUCCESSFULY!')

    def insert_table_tourism(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = TourismCategory()
                category = TourismCategory.objects.all().filter(type=row['category']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']
                if not Tourism.objects.filter(name=row['name']).exists():
                    geo = self.trans_geo(row['address'])
                    if geo != 0:
                        tourism = Tourism.objects.create(name=row['name'],
                                                         address=row['address'],
                                                         explanation=row['explanation'],
                                                         lat=geo['lat'],
                                                         log=geo['long'],
                                                         tour_category=c,
                                                         image=i)
                        print(f' Tourism >>>> {tourism}')
        print('Tourism DATA UPLOADED SUCCESSFULY!')

    def insert_category_activity(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='activity').values()[0]
                c.id = category['id']
                if not ActivityCategory.objects.filter(type=row['category']).exists():
                    a = ActivityCategory.objects.create(type=row['category'],
                                                              section=c,
                                                              category=row['section'])
                    print(f' ActivityCategory >>>> {a}')
        print('Activity Category DATA UPLOADED SUCCESSFULY!')

    def insert_table_activity(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = ActivityCategory()
                category = ActivityCategory.objects.all().filter(type=row['category']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']
                if not Activity.objects.filter(name=row['name']).exists():
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
                                                           image=i)
                        print(f' Activity >>>> {activity}')
        print('Activity DATA UPLOADED SUCCESSFULY!')

    def insert_category_plane(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='plane').values()[0]
                c.id = category['id']
                if not PlaneCategory.objects.filter(type=row['depAirportNm']+"-"+row['arrAirportNm']).exists():
                    a = PlaneCategory.objects.create(type=row['depAirportNm']+"-"+row['arrAirportNm'],
                                                              section=c,
                                                              category=row['type'])
                    print(f' Plane Category >>>> {a}')
        print('Plane Category DATA UPLOADED SUCCESSFULY!')

    def insert_table_plane(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
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
                    print(f' Plane >>>> {plane}')
        print('Plane DATA UPLOADED SUCCESSFULY!')

    def insert_category_restaurant(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='restaurant').values()[0]
                c.id = category['id']
                if not RestaurantCategory.objects.filter(type=row['category']).exists():
                    a = RestaurantCategory.objects.create(type=row['category'],
                                                          category=c)
                    print(f' Restaurant Category >>>> {a}')
        print('Restaurant Category DATA UPLOADED SUCCESSFULY!')

    def insert_table_restaurant(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = RestaurantCategory()
                category = RestaurantCategory.objects.all().filter(type=row['category']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']
                if not Restaurant.objects.filter(name=row['name']).exists():
                    geo = self.trans_geo(row['address'])
                    if geo != 0:
                        restaurant = Restaurant.objects.create(name=row['name'],
                                                               loc=row['address'],
                                                               recommend=row['food'],
                                                               res_category=c,
                                                               lat=geo['lat'],
                                                               log=geo['long'],
                                                               image=i)
                        print(f' Restaurant >>>> {restaurant}')
        print('Restaurant DATA UPLOADED SUCCESSFULY!')

    def insert_category_accommodation(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='accommodation').values()[0]
                c.id = category['id']
                if not AccommodationCategory.objects.filter(type=row['구분']).exists():
                    a = AccommodationCategory.objects.create(type=row['구분'],
                                                             category=c)
                    print(f' Accommodation Category >>>> {a}')
        print('Accommodation Category DATA UPLOADED SUCCESSFULY!')

    def insert_table_accommodation(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = AccommodationCategory()
                category = AccommodationCategory.objects.all().filter(type=row['구분']).values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']
                if not Accommodation.objects.filter(name=row['name']).exists():
                    geo = self.trans_geo(row['소재지'])
                    if geo != 0:
                        accommodation = Accommodation.objects.create(name=row['name'],
                                                                     loc=row['소재지'],
                                                                     price=row['1박당가격'],
                                                                     contact=row['연락처'],
                                                                     standard_number=row['숙박인원'],
                                                                     lat=geo['lat'],
                                                                     log=geo['long'],
                                                                     acc_category=c,
                                                                     image=i,)
                        print(f' Accommodation >>>> {accommodation}')
        print('Accommodation DATA UPLOADED SUCCESSFULY!')

    def insert_table_olle(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='olle').values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['course-name']).values()[0]
                i.id = image['id']
                if not Olle.objects.filter(name=row['course-name']).exists():
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
        print('Olle DATA UPLOADED SUCCESSFULY!')

    def insert_table_shop(self, csvt):
        with open(f'{csvt}', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                c = Category()
                category = Category.objects.all().filter(category='shop').values()[0]
                c.id = category['id']
                i = Image()
                image = Image.objects.all().filter(name=row['name']).values()[0]
                i.id = image['id']

                if not Shop.objects.filter(name=row['name']).exists():
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
                        print(f' Shop >>>> {shop}')
        print('Shop DATA UPLOADED SUCCESSFULY!')

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
        except IndexError:
            return 0
        except TypeError:
            return 0

    def getAddress(self, keyword):
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + keyword
        headers = {"Authorization": "KakaoAK 851f4e6cf0cce36ebf456a4eb33b94d4"}
        result = json.loads(str(requests.get(url, headers=headers).text))
        status_code = requests.get(url, headers=headers).status_code
        if (status_code != 200):
            return 0
        try:
            match_first = result['documents'][0]
            long = match_first['x']
            lat = match_first['y']
            address = match_first['road_address_name']
            return {'long': long, 'lat': lat}
        except IndexError:
            print('match값이 없을때')
            return 0
        except TypeError:
            print('match값이 2개이상일때')
            x, y, address = '1', '1', '1'
            return 0

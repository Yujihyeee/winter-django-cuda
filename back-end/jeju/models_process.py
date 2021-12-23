import random
from datetime import datetime
import sys

from jeju.serializer import JejuSerializer

sys.getdefaultencoding()

# Create your models here.
from django.http import JsonResponse
from icecream import ic
import os

from image.models import Category

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()

from jeju_data.serializer import RestaurantSerializer, PlaneSerializer, AccommodationSerializer, ActivitySerializer, \
    OlleSerializer, ShopSerializer, TourismSerializer
from jeju_data.models import Plane, PlaneCategory, Accommodation, Restaurant, Olle, Activity, Tourism, Shop
from user.models import User
from jeju.models import JejuSchedule



class JejuProcess:
    def __init__(self, option):
        self.startday = datetime.strptime(option['date1'], '%Y-%m-%d')
        self.startloc = option['start']
        self.endday = datetime.strptime(option['date2'], '%Y-%m-%d')
        self.days = (self.endday - self.startday).days + 1
        self.people = option['Number']
        self.user = User.objects.filter(id = option['user']).values()[0]
        self.mbti = self.user['mbti']
        self.mbti_list = self.user['mbti_list']
        self.month = self.startday.month
        self.relationship = option['relationship']

    def process(self):
        mbti = self.mbti_set()
        plane = self.plane()
        accommodation = self.accommodation(mbti)
        activity = self.activity(mbti)
        olle = self.olle()

        return plane, accommodation, activity, olle

    def process_days(self, choice):
        print('=======================')
        print(f'여유날 : {self.days}')
        print('=======================')
        day = self.day_set(choice)
        return day

    def process_save_days(self, choice):
        day = self.save_day_set(choice)
        return day


    def mbti_set(self):
        e = self.mbti_list.count('e')
        s = self.mbti_list.count('s')
        t = self.mbti_list.count('t')
        j = self.mbti_list.count('j')
        return e, s, t, j


    def plane(self):
        category1 = PlaneCategory.objects.filter(type__istartswith=self.startloc).values()[0]
        category2 = PlaneCategory.objects.filter(type__iendswith=self.startloc).values()[0]

        if self.relationship == '가족' or '중요한 분':
            dels, arls = [], []
            if Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category1['id'], depPlandTime__hour__in=[8, 9, 10, 11]) == None:
                family = Plane.objects.filter(plane_category_id=category1['id'], depPlandTime__hour__in=[8, 9, 10, 11])
                [dels.append(i['id']) for i in family.values('id')]

                family = Plane.objects.filter(plane_category_id=category2['id'], depPlandTime__hour__in=[17, 18, 19, 20])
                [arls.append(i['id']) for i in family.values('id')]

            else:
                family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category1['id'],
                                              depPlandTime__hour__in=[8, 9, 10, 11])
                [dels.append(i['id']) for i in family.values('id')]

                family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category2['id'],
                                              depPlandTime__hour__in=[17, 18, 19, 20])
                [arls.append(i['id']) for i in family.values('id')]
            # departure = random.sample(dels, 3)  # 3개 추천
            departure = random.sample(dels, (3 if len(dels) > 3 else len(dels)))  # 3개 추천
            departure = Plane.objects.filter(id__in=departure).values()
            arrival = random.sample(arls, (3 if len(dels) > 3 else len(dels)))  # 3개 추천
            arrival = Plane.objects.filter(id__in=arrival).values()

            serializer1 = PlaneSerializer(departure, many=True)
            serializer2 = PlaneSerializer(arrival, many=True)

            return serializer1, serializer2

        else:
            dels, arls = [], []

            nofamily = Plane.objects.filter(plane_category_id=category1['id'],
                                            depPlandTime__hour__in=[6, 7, 8, 9, 10]).exclude(airlineNm='AAR' or 'KAL')
            [dels.append(i['id']) for i in nofamily.values('id')]
            departure = random.sample(dels, (3 if len(dels) > 3 else len(dels)))  # 3개 추천
            departure = Plane.objects.filter(id__in=departure).values()

            nofamily = Plane.objects.filter(plane_category_id=category2['id'],
                                            depPlandTime__hour__in=[18, 19, 20, 21, 22]).exclude(airlineNm='AAR' or 'KAL')
            [arls.append(i['id']) for i in nofamily.values('id')]
            arrival = random.sample(arls, (3 if len(dels) > 3 else len(dels)))  # 3개 추천
            arrival = Plane.objects.filter(id__in=arrival).values()

            serializer1 = PlaneSerializer(departure, many=True)
            serializer2 = PlaneSerializer(arrival, many=True)

            return serializer1, serializer2


    def accommodation(self, mbti):
        # self.mbti_list[3] = q11 숙소를 구할 때
        ls = []
        if self.mbti_list[3] == 'e' and self.relationship != '가족' or '중요한 분':
            guesthouse = Accommodation.objects.filter(acc_category_id=3)
            [ls.append(i['id']) for i in guesthouse.values('id')]
            acc = random.sample(ls, 3)  # 3개
            acc = Accommodation.objects.filter(id__in=acc).values()
            serializer = AccommodationSerializer(acc, many=True)
            return serializer

        elif self.relationship == '가족' or '중요한 분':
            if self.mbti_list[3] == 'i' and self.people >= 4:
                pull = Accommodation.objects.filter(acc_category_id=1)
                [ls.append(i['id']) for i in pull.values('id')]
                acc = random.sample(ls, 3)  # 3개
                acc = Accommodation.objects.filter(id__in=acc).values()
                serializer = AccommodationSerializer(acc, many=True)
                return serializer

            else:
                pull = Accommodation.objects.filter(acc_category_id__in=[1, 4])
                [ls.append(i['id']) for i in pull.values('id')]
                acc = random.sample(ls, 3)  # 3개
                acc = Accommodation.objects.filter(id__in=acc).values()
                serializer = AccommodationSerializer(acc, many=True)
                return serializer

        else:
            guesthouse = Accommodation.objects.filter(acc_category_id__in=[2, 4])
            [ls.append(i['id']) for i in guesthouse.values('id')]
            acc = random.sample(ls, 3)  # 3개
            acc = Accommodation.objects.filter(id__in=acc).values()
            serializer = AccommodationSerializer(acc, many=True)
            return serializer

    def activity(self, mbti):
        e, s, t, j = mbti
        days = int((self.days * 1.5) + 1)
        ls, ls1, ls2 = [], [], []
        if e == 3:
            activity = Activity.objects.filter(act_category__category='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity = random.sample(ls, (days if len(ls) > days else len(ls)))  # 여러개
            activity = Activity.objects.filter(id__in=activity).values()
            serializer = ActivitySerializer(activity, many=True)
            return serializer



        elif e == 2:
            day = int(days * 0.7)
            activity = Activity.objects.filter(act_category__category='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity1 = random.sample(ls, (day if len(ls) > day else len(ls)))  # 여러개
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls1.append(i['id']) for i in activity.values('id')]
            activity2 = random.sample(ls1, (int(days - day) if len(ls1) > int(days - day) else len(ls1)))  # 여러개
            [ls2.append(i) for i in activity1]
            [ls2.append(i) for i in activity2]
            activity = Activity.objects.filter(id__in=ls2).values()
            serializer = ActivitySerializer(activity, many=True)
            return serializer

        elif e == 1:
            day = int(self.days * 0.8)
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity1 = random.sample(ls, (day if len(ls) > day else len(ls)))  # 여러개
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls1.append(i['id']) for i in activity.values('id')]
            activity2 = random.sample(ls1, (int(days - day) if len(ls1) > int(days - day) else len(ls1)))  # 여러개
            [ls2.append(i) for i in activity1]
            [ls2.append(i) for i in activity2]
            activity = Activity.objects.filter(id__in=ls2).values()
            serializer = ActivitySerializer(activity, many=True)
            return serializer

        else:
            activty = Activity.objects.exclude(act_category__category='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            activity = random.sample(ls, (days if len(ls) > days else len(ls)))  # 여러개
            activity = Activity.objects.filter(id__in=activity).values()
            serializer = ActivitySerializer(activity, many=True)
            return serializer

    def olle(self):
        days = int(self.days * 0.30)
        ls, ls2 = [], []
        if self.mbti_list[2] == 'e' or self.mbti_list[8] == 't':
            if self.days < 7:
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                olle = random.sample(ls, 2)  #  2개
                oleum = TourismSerializer(Tourism.objects.filter(name__in=olle).values(), many=True)
                olle = OlleSerializer(Olle.objects.filter(name__in=olle).values(), many=True)
                return olle, oleum
            else:
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                olle =  random.sample(ls, (days if len(ls) > days else len(ls)))   # 여러개
                oleum = TourismSerializer(Tourism.objects.filter(name__in=olle).values(), many=True)
                olle = OlleSerializer(Olle.objects.filter(name__in=olle).values(), many=True)
                return olle, oleum
        else:
            return 0

    def activty_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance', [i['lat'], i['log'], i['lat'], at])[:2]
        a = RestaurantSerializer(a, many=True).data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance", [i['lat'], i['log'], i['lat'], bt])[:2]
        b = TourismSerializer(b, many=True).data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Activity.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
        c = ActivitySerializer(c, many=True).data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        d = ShopSerializer(d, many=True).data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day-{i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def olle_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        a = RestaurantSerializer(a, many=True).data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        b = TourismSerializer(b, many=True).data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Olle.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM olle ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
        c = OlleSerializer(c, many=True).data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        d = ShopSerializer(d, many=True).data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day-{i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def oleum_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        a = RestaurantSerializer(a, many=True).data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        b = TourismSerializer(b, many=True).data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism ORDER BY distance",
            [i['lat'], i['log'], i['lat']])[:1]
        c = TourismSerializer(c, many=True).data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        d = ShopSerializer(d, many=True).data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day-{i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def accommodation_values(self, dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id):

        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        a = RestaurantSerializer(a, many=True).data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12)  ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        b = TourismSerializer(b, many=True).data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        d = ShopSerializer(d, many=True).data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"{j}day-{i['name']}"] = a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def day_set(self, choice):
        plane = choice['plane']
        acc = choice['acc']
        activity = choice['activty']

        dic = {}

        if choice['olle'] == None:
            count = len(activity)
            day = int(self.days - count)
            if day > 0:
                activty = Activity.objects.filter(id__in=activity).values()
                acc = Accommodation.objects.filter(id=acc).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for j in range(day):
                    for i in acc.values():
                        self.accommodation_values(dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id)

            else:
                activty = Activity.objects.filter(id__in=activity).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)

        else:
            olle = choice['olle']
            count = len(activity) + len(olle)
            day = int(self.days - count)
            if day > 0:
                activty = Activity.objects.filter(id__in=activity).values()
                acc = Accommodation.objects.filter(id=acc).values()
                oleum = Tourism.objects.filter(name__in=olle).values()
                olle = Olle.objects.filter(name__in=olle).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in oleum.values():
                    self.oleum_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in olle.values():
                    self.olle_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for j in range(day):
                    for i in acc.values():
                        self.accommodation_values(dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id)
            else:
                activty = Activity.objects.filter(id__in=activity).values()
                oleum = Tourism.objects.filter(name__in=olle).values()
                olle = Olle.objects.filter(name__in=olle).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in oleum.values():
                    self.oleum_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in olle.values():
                    self.olle_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)


        return dic, plane, choice['acc']

    def save_day_set(self, choice):
        plane = choice['plane']
        acc = choice['acc']
        activity = choice['activty']
        dic = {}
        print(choice['olle'])
        if choice['olle'] == []:
            print('************************  if')

            count = len(activity)
            day = int(self.days - count)
            if day > 0:
                activty = Activity.objects.filter(id__in=activity).values()
                acc = Accommodation.objects.filter(id=acc).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for j in range(day):
                    for i in acc.values():
                        self.accommodation_values(dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id)

            else:
                activty = Activity.objects.filter(id__in=activity).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)

            except_restaurant_id.remove(0)
            except_tourism_id.remove(0)
            except_shop_id.remove(0)

            u = User()
            user = User.objects.all().filter(id=self.user['id']).values()[0]
            u.id = user['id']
            c = Category()
            category = Category.objects.all().filter(category='recommend').values()[0]
            c.id = category['id']
            ac = Accommodation()
            print(choice['acc'])
            accommodation = Accommodation.objects.filter(id=choice['acc']).values()[0]
            print(accommodation)
            ac.id = accommodation['id']

            p = ','.join(str(i) for i in plane)
            a = ','.join(str(i) for i in activity)
            r = ','.join(str(i) for i in except_restaurant_id)
            t = ','.join(str(i) for i in except_tourism_id)
            s = ','.join(str(i) for i in except_shop_id)


            today = datetime.date.today()
            print(today)
            # today = f"{str(today)[0:4]}-{str(today)[5:7]}-{str(today)[8:10]}"
            dday = self.startday - today

            save_day = JejuSchedule.objects.create(user=u, startday=self.startday, endday=self.endday, day=self.days, startloc=self.startloc, people=self.people, relationship=self.relationship, category=c,
                                                   plane=p, acc=ac, activity=a, restaurant=r, tourism=t, shop=s, schedule=f"{dic}", dday=dday)
            print(f' 1 >>>> {save_day}')

            startday = {"startday": self.startday}
            endday = {"endday": self.endday}
            days = {"days": self.days}
            people = {"people": self.people}
            user = {"user": self.user['id']}
            relationship = {"relationship": self.relationship}

            return dic, plane, choice['acc'], activity, except_restaurant_id, except_tourism_id, except_shop_id, startday, endday, days, people, user, relationship

        else:
            print('************************  else')
            olle = choice['olle']
            count = len(activity) + len(olle)
            day = int(self.days - count)
            if day > 0:
                activty = Activity.objects.filter(id__in=activity).values()
                acc = Accommodation.objects.filter(id=acc).values()
                oleum = Tourism.objects.filter(name__in=olle).values()
                olle1 = Olle.objects.filter(name__in=olle).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in oleum.values():
                    self.oleum_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in olle1.values():
                    self.olle_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for j in range(day):
                    for i in acc.values():
                        self.accommodation_values(dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id)
            else:
                activty = Activity.objects.filter(id__in=activity).values()
                oleum = Tourism.objects.filter(name__in=olle).values()
                olle1 = Olle.objects.filter(name__in=olle).values()
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                for i in activty.values():
                    self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in oleum.values():
                    self.oleum_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
                for i in olle1.values():
                    self.olle_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)

            except_restaurant_id.remove(0)
            except_tourism_id.remove(0)
            except_shop_id.remove(0)

            u = User()
            user = User.objects.all().filter(id=self.user['id']).values()[0]
            u.id = user['id']
            c = Category()
            category = Category.objects.all().filter(category='recommend').values()[0]
            c.id = category['id']
            ac = Accommodation()
            accommodation = Accommodation.objects.filter(id=choice['acc']).values()[0]
            ac.id = accommodation['id']

            p = ','.join(str(i) for i in plane)
            a = ','.join(str(i) for i in activity)
            o = ','.join(str(i) for i in olle)
            r = ','.join(str(i) for i in except_restaurant_id)
            t = ','.join(str(i) for i in except_tourism_id)
            s = ','.join(str(i) for i in except_shop_id)

            # plane_data = Plane.objects.filter(id__in=plane).values()
            dic["plane"] = PlaneSerializer(Plane.objects.filter(id__in=plane).values(), many=True).data


            # acc_data = Accommodation.objects.filter(id=acc).values()
            dic["acc"] = AccommodationSerializer(Accommodation.objects.filter(id=choice['acc']).values(), many=True).data

            today = datetime.date.today()
            # today = f"{str(today)[0:4]}-{str(today)[5:7]}-{str(today)[8:10]}"
            dday = self.startday - today

            # schedule_dic = {"plane" : plane_data} + {"acc": acc_data} + dic

            save_day = JejuSchedule.objects.create(user=u, startday=self.startday, endday=self.endday, day=self.days, startloc=self.startloc,
                                                   people=self.people, relationship=self.relationship, category=c,
                                                   plane=p, acc=ac, activity=a, olle=o, restaurant=r, tourism=t, shop=s, schedule=f"{dic}", dday=dday)
            print(f' 1 >>>> {save_day}')

            startday = {"startday": self.startday}
            endday = {"endday": self.endday}
            days = {"days": self.days}
            people = {"people": self.people}
            user = {"user": self.user['id']}
            relationship = {"relationship": self.relationship}

            return dic, plane, choice['acc'], activity, except_restaurant_id, except_tourism_id, except_shop_id, startday, endday, days, people, user, relationship, olle

class RDATA:
    def pr_days(self, user_id):
        today = datetime.date.today()
        print(today)
        jejuSchedule = JejuSchedule.objects.raw(
            f"select * from jeju_schedule where user_id = {user_id} and startday > '{today}';")
        # [print(i) for i in list(jejuSchedule)]
        serializer = JejuSerializer(jejuSchedule, many=True)
        dday = []
        [dday.append(i-today) for i in jejuSchedule.values('startday')]
        # dday = jejuSchedule['startday'] - today
        print(dday)
        return serializer.data

if __name__ == '__main__':
    option = {"date1": '2021-05-30', "date2": '2021-06-09', 'start': 'gmp', 'Number': 4, 'user': 2, 'relationship': 'family'}
    a = JejuProcess(option)
    a.process()
    choice = {'acc' : 15, 'activty' : [1, 5, 6, 20, 15, 17, 18], 'olle': ['거문오름']}
    # a.process_days(choice)
    choice = {"date1": "2021-05-30", "date2": "2021-06-09", "start": "gmp", "Number": 4, "user": 2, "relationship": "family", "plane" : [24, 127], "acc": 15, "activty": [1,5,6,23,29,17,14], "olle": ["무릉-용수 올레", "금악오름"] }
    a.save_day_set(choice)


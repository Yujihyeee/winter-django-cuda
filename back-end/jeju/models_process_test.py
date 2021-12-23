import random
from datetime import datetime

# Create your models here.
from django.http import JsonResponse
from icecream import ic
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

import django
django.setup()

from jeju_data.serializer import RestaurantSerializer, PlaneSerializer, AccommodationSerializer, ActivitySerializer, \
    OlleSerializer, ShopSerializer, TourismSerializer
from jeju_data.models import Plane, PlaneCategory, Accommodation, Restaurant, Olle, Activity, Tourism, Shop
from user.models import User



class JejuProcessTest:
    def __init__(self, option):
        print("시작하자")
        print(option)
        self.startday = datetime.strptime(option['date1'], '%Y-%m-%d')
        self.startloc = option['start']
        self.endday = datetime.strptime(option['date2'], '%Y-%m-%d')
        self.days = (self.endday - self.startday).days
        self.people = option['Number']
        self.user = User.objects.filter(id = option['user']).values()[0]
        self.mbti = self.user['mbti']
        self.mbti_list = self.user['mbti_list']
        self.month = self.startday.month
        self.relationship = option['relationship']
        print(self.user)

    def process(self):
        print('################### mbti ###################')
        mbti = self.mbti_set()
        print(mbti)
        # print('################### plane ###################')
        # plane = self.plane()
        # print(plane)
        print('################### accommodation ###################')
        accommodation = self.accommodation(mbti)
        print(accommodation)
        # print('################### activty ###################')
        # activty = self.activty(mbti)
        # print(activty)
        # print('################### olle ###################')
        # olle = self.olle(mbti)
        # print(olle)
        # print('################### test ###################')
        # test = self.test(activty, olle)
        # print(test)

    def process_days(self, acc, activty, olle):
        print('################### test ###################')
        # test = self.test_day(acc, activty, olle)
        # print(test)
        # # test_day = random.shuffle(test)
        # [print(i) for i in test]
        test = self.test_day_set(acc, activty, olle)
        print(test)
        # test_day = random.shuffle(test)
        [print(i) for i in test]

        # print('################### tourism ###################')
        # tourism = self.tourism(activty, olle)
        # print(tourism)
        # print('################### restaurant ###################')
        # restaurant = self.restaurant(accommodation)
        # print(restaurant)
        # print('################### shop ###################')
        # shop = self.shop(activty, olle)
        # print(shop)

        # return plane, accommodation, activty, olle, tourism, restaurant, shop

    def mbti_set(self):
        e = self.mbti_list.count('e')
        s = self.mbti_list.count('s')
        t = self.mbti_list.count('t')
        j = self.mbti_list.count('j')

        return e, s, t, j


    def plane(self):
        category1 = PlaneCategory.objects.filter(type__istartswith=self.startloc).values()[0]
        category2 = PlaneCategory.objects.filter(type__iendswith=self.startloc).values()[0]

        if self.relationship == 'family':
            dels, arls = [],[]

            family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category1['id'],
                                          depPlandTime__hour__in=[8, 9, 10, 11])
            [dels.append(i['id']) for i in family.values('id')]
            [print(i) for i in dels]
            # departure = {'departure': random.sample(dels, 3)}  # 3개 추천
            # departure = {'departure': dels[random.randint(0, len(dels)-1)]}  # 1개 추천
            # departure = random.sample(dels, 3)  # 3개 추천
            departure = [dels[random.randint(0, len(dels) - 1)]]  # 1개 추천
            departure = Plane.objects.filter(id__in=departure).values()
            print(departure)

            family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id=category2['id'],
                                          depPlandTime__hour__in=[17, 18, 19, 20])
            [arls.append(i['id']) for i in family.values('id')]
            [print(i) for i in arls]
            # arrival = {'arrival': random.sample(arls, 3)}  # 3개 추천
            # arrival = {'arrival': arls[random.randint(0, len(arls) - 1)]}  # 1개 추천
            # arrival = random.sample(arls, 3)  # 3개 추천
            arrival = [arls[random.randint(0, len(arls) - 1)]]  # 1개 추천
            arrival = Plane.objects.filter(id__in=arrival).values()
            print(arrival)
            # a = departure, arrival
            # print('################### a #####################')
            # print(a)
            # print('########################################')
            serializer1 = PlaneSerializer(departure, many=True)
            print(serializer1.data)
            serializer2 = PlaneSerializer(arrival, many=True)
            print(serializer2.data)

            return JsonResponse(data=(serializer1.data, serializer2.data), safe=False)

        else:
            dels, arls = []

            nofamily = Plane.objects.filter(plane_category_id=category1['id'],
                                            depPlandTime__hour__in=[6, 7, 8, 9, 10]).exclude(airlineNm='AAR' or 'KAL')
            [dels.append(i['id']) for i in nofamily.values('id')]
            [print(i) for i in dels]
            # departure = {'departure': random.sample(dels, 3)}  # 3개 추천
            # departure = {'departure': dels[random.randint(0, len(dels)-1)]}  # 1개 추천
            # departure = random.sample(dels, 3)  # 3개 추천
            departure = [dels[random.randint(0, len(dels) - 1)]]  # 1개 추천
            departure = Plane.objects.filter(id__in=departure).values()
            print(departure)

            nofamily = Plane.objects.filter(plane_category_id=category2['id'],
                                            depPlandTime__hour__in=[18, 19, 20, 21, 22]).exclude(airlineNm='AAR' or 'KAL')
            [arls.append(i['id']) for i in nofamily.values('id')]
            [print(i) for i in arls]
            # arrival = {'arrival': random.sample(arls, 3)}  # 3개 추천
            # arrival = {'arrival': arls[random.randint(0, len(arls) - 1)]}  # 1개 추천
            # arrival = random.sample(arls, 3)  # 3개 추천
            arrival = [arls[random.randint(0, len(arls) - 1)]]  # 1개 추천
            arrival = Plane.objects.filter(id__in=arrival).values()
            print(arrival)
            serializer1 = PlaneSerializer(departure, many=True)
            print(serializer1.data)
            serializer2 = PlaneSerializer(arrival, many=True)
            print(serializer2.data)

            return JsonResponse(data=(serializer1.data, serializer2.data), safe=False)

        # nols, yesls = [], []
        # # [nols.append(i.values()) for i in nofamily.values('id')]
        # [nols.append(i['id']) for i in nofamily.values('id')]
        # # print(nols)
        # [print(i) for i in nols]
        # # print(nols[random.randint(0, len(nols))])
        # print(nols[random.randint(0, len(nols) - 1)])
        #
        # [yesls.append(i['id']) for i in family.values('id')]
        # [print(i) for i in yesls]
        # print(yesls[random.randint(0, len(yesls) - 1)])
        #
        # # if self.relationship == 'family':
        # #     random
        # # nofamily = Plane.objects.exclude(airlineNm='AAR' or 'KAL')
        # # family = Plane.objects.filter(airlineNm='AAR' or 'KAL')
        # # nols, yesls = [], []
        # # [nols.append(i) for i in nofamily.values('airlineNm')]
        # # print(nols)
        # # category1 = PlaneCategory.objects.filter(type__icontains= f"{self.startloc}-cju")
        # category1 = PlaneCategory.objects.filter(type__istartswith=self.startloc).values()[0]
        # nofamily = Plane.objects.filter(plane_category_id=category1['id']).exclude(airlineNm='AAR' or 'KAL')
        # family = Plane.objects.filter(airlineNm='AAR' or 'KAL', plane_category_id='1')
        # nols, yesls = [], []
        # # [nols.append(i.values()) for i in nofamily.values('id')]
        # [nols.append(i['id']) for i in nofamily.values('id')]
        # # [print(i) for i in nols]
        # print(nols[random.randint(0, len(nols))])

    def accommodation(self, mbti):
        # self.mbti_list[3] = q11 숙소를 구할 때
        e, s, t, j = mbti
        print(e)
        if self.mbti_list[3] == 'e' and self.relationship != 'family':
            ls = []
            guesthouse = Accommodation.objects.filter(acc_category_id=3)
            [ls.append(i['id']) for i in guesthouse.values('id')]
            [print(i) for i in ls]
            acc = random.sample(ls, 3)  # 3개
            # acc = [ls[random.randint(0, len(ls) - 1)]]  # 1개
            acc = Accommodation.objects.filter(id__in=acc).values()
            print(acc)
            serializer = AccommodationSerializer(acc, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)


        if self.relationship == 'family':
            if self.mbti_list[3] == 'i' and self.people >= 4:
                ls = []
                pull = Accommodation.objects.filter(acc_category_id=1)
                [ls.append(i['id']) for i in pull.values('id')]
                [print(i) for i in ls]
                acc = random.sample(ls, 3)  # 3개
                # acc = [ls[random.randint(0, len(ls) - 1)]]  # 1개
                acc = Accommodation.objects.filter(id__in=acc).values()
                print(acc)
                serializer = AccommodationSerializer(acc, many=True)
                print(serializer.data)

                return JsonResponse(data=serializer.data, safe=False)
            else:
                ls = []
                pull = Accommodation.objects.filter(acc_category_id__in=[1, 4])
                [ls.append(i['id']) for i in pull.values('id')]
                [print(i) for i in ls]
                acc = random.sample(ls, 3)  # 3개
                # acc = [ls[random.randint(0, len(ls) - 1)]]  # 1개
                acc = Accommodation.objects.filter(id__in=acc).values()
                print(acc)
                serializer = AccommodationSerializer(acc, many=True)
                print(serializer.data)

                return JsonResponse(data=serializer.data, safe=False)
        else:
            ls = []
            guesthouse = Accommodation.objects.filter(acc_category_id__in=[2, 4])
            [ls.append(i['id']) for i in guesthouse.values('id')]
            [print(i) for i in ls]
            # acc = random.sample(ls, 3)  # 3개
            acc = [ls[random.randint(0, len(ls) - 1)]]  # 1개
            acc = Accommodation.objects.filter(id__in=acc).values()
            print(acc)
            serializer = AccommodationSerializer(acc, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)

    def activity(self, mbti):
        e, s, t, j = mbti
        self.days = int(self.days * 1.5)
        print(self.mbti_list[2], self.mbti_list[8])
        ls, ls1, ls2 = [], [], []
        if e == 3:
            print('e = 3')
            activity = Activity.objects.filter(act_category__category__in='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity = random.sample(ls, int(self.days))  # 여러개
            activity = Activity.objects.filter(id__in=activity).values()
            print(activity)
            serializer = ActivitySerializer(activity, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)

        if e == 2:
            print('e == 2')
            day = int(self.days * 0.7)
            activity = Activity.objects.filter(act_category__category='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity1 = random.sample(ls, day)  # 여러개
            # activity1 =  [ls[random.randint(0, len(ls) - 1)]]  # 1개
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls1.append(i['id']) for i in activity.values('id')]
            activity2 = random.sample(ls1, int(self.days - day))  # 여러개
            # activity2 = [ls[random.randint(0, len(ls) - 1)]]  # 1개
            activity = activity1, activity2
            print(activity)
            activity = Activity.objects.filter(id__in=activity).values()
            print(activity)
            serializer = ActivitySerializer(activity, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)

        if e == 1:
            print('e == 1')
            day = int(self.days * 0.8)
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls.append(i['id']) for i in activity.values('id')]
            activity1 = random.sample(ls, day)  # 여러개
            # activity1 = [ls[random.randint(0, len(ls) - 1)]]  # 1개
            activity = Activity.objects.exclude(act_category__category='액티비티')
            [ls1.append(i['id']) for i in activity.values('id')]
            activity2 = random.sample(ls1, int(self.days - day))  # 여러개
            # activity2 = [ls[random.randint(0, len(ls) - 1)]]  # 1개

            activity = activity1, activity2
            print(activity)
            activity = Activity.objects.filter(id__in=activity).values()
            print(activity)
            serializer = ActivitySerializer(activity, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)

        else:
            print('e == 0')
            activty = Activity.objects.exclude(act_category__category__in='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            [print(i) for i in ls]
            activity = random.sample(ls, int(self.days))  # 여러개
            # activty = [ls[random.randint(0, len(ls) - 1)]]  # 1개
            activity = Activity.objects.filter(id__in=activity).values()
            print(activity)
            serializer = ActivitySerializer(activity, many=True)
            print(serializer.data)

            return JsonResponse(data=serializer.data, safe=False)

    def olle(self, mbti):
        e, s, t, j = mbti
        print(int(self.days * 0.30))
        days = int(self.days * 0.30)
        if self.mbti_list[2] == 'e' or self.mbti_list[8] == 't':
            if self.days < 7 :
                ls, ls2 = [], []
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                print(ls)
                olle = random.sample(ls, 2)  #  여러개
                # olle = [ls[random.randint(0, len(ls) - 1)]]   # 한개
                olle = Olle.objects.filter(id__in=olle).values()
                print(olle)
                serializer = OlleSerializer(olle, many=True)
                print(serializer.data)

                return JsonResponse(data=serializer.data, safe=False)
            else:
                ls, ls2 = [], []
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                print(ls)
                olle =  random.sample(ls, days)   # 여러개
                # olle = [ls[random.randint(0, len(ls) - 1)]]  # 한개
                olle = Olle.objects.filter(id__in=olle).values()
                print(olle)
                serializer = OlleSerializer(olle, many=True)
                print(serializer.data)
                return JsonResponse(data=serializer.data, safe=False)
        else:
            return 0

    def activty_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance', [i['lat'], i['log'], i['lat'], at])[:2]
        serializer_a = RestaurantSerializer(a, many=True)
        a = serializer_a.data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        print(except_restaurant_id)
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance", [i['lat'], i['log'], i['lat'], bt])[:2]
        serializer_b = TourismSerializer(b, many=True)
        b = serializer_b.data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Activity.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
        serializer_c = ActivitySerializer(c, many=True)
        c = serializer_c.data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        serializer_d = ShopSerializer(d, many=True)
        d = serializer_d.data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day: {i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def olle_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        serializer_a = RestaurantSerializer(a, many=True)
        a = serializer_a.data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        serializer_b = TourismSerializer(b, many=True)
        b = serializer_b.data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Olle.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM olle ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
        serializer_c = OlleSerializer(c, many=True)
        c = serializer_c.data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        serializer_d = ShopSerializer(d, many=True)
        d = serializer_d.data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day: {i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def oleum_values(self, dic, i, except_restaurant_id, except_tourism_id, except_shop_id):
        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        serializer_a = RestaurantSerializer(a, many=True)
        a = serializer_a.data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        print(except_restaurant_id)
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12) ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        serializer_b = TourismSerializer(b, many=True)
        b = serializer_b.data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        c = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism ORDER BY distance",
            [i['lat'], i['log'], i['lat']])[:1]
        serializer_c = TourismSerializer(c, many=True)
        c = serializer_c.data
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        serializer_d = ShopSerializer(d, many=True)
        d = serializer_d.data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"day: {i['name']}"] = c + a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def accommodation_values(self, dic, i, j, except_restaurant_id, except_tourism_id, except_shop_id):

        at = tuple(except_restaurant_id)
        a = Restaurant.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
            'AS distance FROM restaurant where id not in %s ORDER BY distance',
            [i['lat'], i['log'], i['lat'], at])[:2]
        serializer_a = RestaurantSerializer(a, many=True)
        a = serializer_a.data
        [except_restaurant_id.append(list(i.values())[0]) for i in a]
        bt = tuple(except_tourism_id)
        b = Tourism.objects.raw(
            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
            "AS distance FROM tourism where id not in %s and tour_category_id not in (8, 12)  ORDER BY distance",
            [i['lat'], i['log'], i['lat'], bt])[:2]
        serializer_b = TourismSerializer(b, many=True)
        b = serializer_b.data
        [except_tourism_id.append(list(i.values())[0]) for i in b]
        dt = tuple(except_shop_id)
        d = Shop.objects.raw(
            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
            [i['lat'], i['log'], i['lat'], dt])[:1]
        serializer_d = ShopSerializer(d, many=True)
        d = serializer_d.data
        [except_shop_id.append(list(i.values())[0]) for i in d]
        dic[f"추가-{j}day: {i['name']}"] = a + b + d

        return dic, except_restaurant_id, except_tourism_id, except_shop_id

    def test_day_set(self, acc, activty, olle):
        count = len(activty['activty']) + len(olle['olle'])
        print(count)
        day = int(self.days - count)
        print(day)
        dic = {}
        if day > 0:
            activty = Activity.objects.filter(id__in=activty['activty']).values()
            acc = Accommodation.objects.filter(id=acc['acc']).values()
            oleum = Tourism.objects.filter(name__in=olle['olle']).values()
            olle = Olle.objects.filter(name__in=olle['olle']).values()
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
            activty = Activity.objects.filter(id__in=activty['activty']).values()
            oleum = Tourism.objects.filter(name__in=olle['olle']).values()
            olle = Olle.objects.filter(name__in=olle['olle']).values()
            except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
            for i in activty.values():
                self.activty_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
            for i in oleum.values():
                self.oleum_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)
            for i in olle.values():
                self.olle_values(dic, i, except_restaurant_id, except_tourism_id, except_shop_id)

        return dic

    def test_day(self, acc, activty, olle):
        count = len(activty['activty']) + len(olle['olle'])
        print(count)
        day = int(self.days - count)
        print(day)
        dic = {}
        if day > 0 :
            activty = Activity.objects.filter(id__in=activty['activty']).values()
            acc = Accommodation.objects.filter(id=acc['acc']).values()
            if Olle.objects.filter(name__in=olle['olle']).values() != None:
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                olle = Olle.objects.filter(name__in=olle['olle']).values()
                for i in activty.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance', [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance", [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Activity.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = ActivitySerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d

                for i in olle.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s  ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Olle.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM olle ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = OlleSerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d
                for j in range(day):
                    for i in acc.values():
                        at = tuple(except_restaurant_id)
                        a = Restaurant.objects.raw(
                            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                            'AS distance FROM restaurant where id not in %s ORDER BY distance',
                            [i['lat'], i['log'], i['lat'], at])[:2]
                        serializer_a = RestaurantSerializer(a, many=True)
                        a = serializer_a.data
                        [except_restaurant_id.append(list(i.values())[0]) for i in a]
                        bt = tuple(except_tourism_id)
                        b = Tourism.objects.raw(
                            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                            "AS distance FROM tourism where id not in %s  ORDER BY distance",
                            [i['lat'], i['log'], i['lat'], bt])[:2]
                        serializer_b = TourismSerializer(b, many=True)
                        b = serializer_b.data
                        [except_tourism_id.append(list(i.values())[0]) for i in b]
                        dt = tuple(except_shop_id)
                        d = Shop.objects.raw(
                            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                            [i['lat'], i['log'], i['lat'], dt])[:1]
                        serializer_d = ShopSerializer(d, many=True)
                        d = serializer_d.data
                        [except_shop_id.append(list(i.values())[0]) for i in d]
                        dic[f"추가-{j}day: {i['name']}"] = a + b + d


            else:
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                oleum = Tourism.objects.filter(name__in=olle['olle']).values()
                for i in activty.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Activity.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = ActivitySerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d
                for i in oleum.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM olle WHERE tour_category_id = 8, 12 ORDER BY distance",
                        [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = TourismSerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d
                for j in range(day):
                    for i in acc.values():
                        a = Restaurant.objects.raw(
                            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                            '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                            'AS distance FROM restaurant where id not in %s ORDER BY distance',
                            [i['lat'], i['log'], i['lat'], at])[:2]
                        serializer_a = RestaurantSerializer(a, many=True)
                        a = serializer_a.data
                        [except_restaurant_id.append(list(i.values())[0]) for i in a]
                        print(except_restaurant_id)
                        bt = tuple(except_tourism_id)
                        b = Tourism.objects.raw(
                            "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                            "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                            "AS distance FROM tourism where id not in %s ORDER BY distance",
                            [i['lat'], i['log'], i['lat'], bt])[:2]
                        serializer_b = TourismSerializer(b, many=True)
                        b = serializer_b.data
                        [except_tourism_id.append(list(i.values())[0]) for i in b]
                        dt = tuple(except_shop_id)
                        d = Shop.objects.raw(
                            'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                            '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                            [i['lat'], i['log'], i['lat'], dt])[:1]
                        serializer_d = ShopSerializer(d, many=True)
                        d = serializer_d.data
                        [except_shop_id.append(list(i.values())[0]) for i in d]
                        dic[f"추가-{j}day: {i['name']}"] = a + b + d
        else:
            activty = Activity.objects.filter(id__in=activty['activty']).values()
            acc = Accommodation.objects.filter(id=acc['acc']).values()
            if Olle.objects.filter(name__in=olle['olle']).values() != None:
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                olle = Olle.objects.filter(name__in=olle['olle']).values()
                for i in activty.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Activity.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = ActivitySerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d

                for i in olle.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s  ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Olle.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM olle ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = OlleSerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d

            else:
                except_restaurant_id, except_tourism_id, except_shop_id = [0], [0], [0]
                oleum = Tourism.objects.filter(name__in=olle['olle']).values()
                for i in activty.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Activity.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = ActivitySerializer(c, many=True)
                    c = serializer_c.data
                    dt = tuple(except_shop_id)
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d
                for i in oleum.values():
                    at = tuple(except_restaurant_id)
                    a = Restaurant.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                        '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                        'AS distance FROM restaurant where id not in %s ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], at])[:2]
                    serializer_a = RestaurantSerializer(a, many=True)
                    a = serializer_a.data
                    [except_restaurant_id.append(list(i.values())[0]) for i in a]
                    print(except_restaurant_id)
                    bt = tuple(except_tourism_id)
                    b = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM tourism where id not in %s ORDER BY distance",
                        [i['lat'], i['log'], i['lat'], bt])[:2]
                    serializer_b = TourismSerializer(b, many=True)
                    b = serializer_b.data
                    [except_tourism_id.append(list(i.values())[0]) for i in b]
                    c = Tourism.objects.raw(
                        "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                        "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                        "AS distance FROM olle WHERE tour_category_id = 8, 12 ORDER BY distance",
                        [i['lat'], i['log'], i['lat']])[:1]
                    serializer_c = TourismSerializer(c, many=True)
                    c = serializer_c.data
                    d = Shop.objects.raw(
                        'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))'
                        '+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop where id not in %s HAVING distance < 4 ORDER BY distance',
                        [i['lat'], i['log'], i['lat'], dt])[:1]
                    serializer_d = ShopSerializer(d, many=True)
                    d = serializer_d.data
                    [except_shop_id.append(list(i.values())[0]) for i in d]
                    dic[f"day: {i['name']}"] = c + a + b + d

        return dic

    def activity_set(self, mbti):
        # self.mbti_list[2] : q13 우리 여행지 가서 뭐 할까? 라는 친구의 말에 우리(나)는?
        # self.mbti_list[8] : q10 우리(나)는 여행지를 선택할 때 주로
        e, s, t, j = mbti
        olle_days = int(self.days * 0.20)
        print(olle_days)
        print(self.mbti_list[2], self.mbti_list[8])
        ls, ls1, ls2 = [], [], []
        if e == 3:
            print('e = 3')
            # activty = Activity.objects.filter(act_category_id__in=[1, 2, 3, 4, 5, 6, 7, 8, 9])
            activty = Activity.objects.filter(act_category__category__in='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            [print(i) for i in ls]
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) < 10:
                print('올레 포함')
                activty = {'activty': random.sample(ls, int(self.days - 1))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty

            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) >= 10:
                print('10일 이상 올레 포함')
                activty = {'activty': random.sample(ls, int(self.days - olle_days))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty

            else:
                print('올레 비포함')
                activty = {'activty': random.sample(ls, int(self.days))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty

        if e == 2:
            print('e == 2')
            day = int(self.days * 0.7)
            days = int(day - olle_days)
            # print(days)
            activty = Activity.objects.filter(act_category__category='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            # [print(i) for i in ls]
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) < 10:
                print('올레 포함')
                activty1 = random.sample(ls, int(day - 1))  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.exclude(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days-day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2 }
                return activty
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) >= 10:
                print('10일 이상 올레 포함')
                activty1 = random.sample(ls, days)  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.exclude(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days - day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2}
                return activty
            else:
                print('올레 비포함')
                activty1 = random.sample(ls, day)  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.exclude(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days - day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2}
                return activty

        if e == 1:
            print('e == 1')
            day = int(self.days * 0.8)
            days = int(day - olle_days)
            print(days)
            activty = Activity.objects.exclude(act_category__category='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            # [print(i) for i in ls]
            if self.mbti_list[2] == 'e' or self.mbti_list[8] == 't' and int(days) < 10:
                print('올레 포함')
                activty1 = random.sample(ls, int(day-1))  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.filter(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days - day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2}
                return activty
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) >= 10:
                print('10일 이상 올레 포함')
                activty1 = random.sample(ls, days)  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.filter(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days - day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2}
                return activty
            else:
                print('올레 비포함')
                activty1 = random.sample(ls, day)  # 여러개
                # activty1 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = Activity.objects.exclude(act_category__category='액티비티')
                [ls1.append(i['id']) for i in activty.values('id')]
                activty2 = random.sample(ls1, int(self.days - day))  # 여러개
                # activty2 = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                activty = {'activty': activty1 + activty2}
                return activty

        else:
            print('e == 0')
            activty = Activity.objects.exclude(act_category__category__in='액티비티')
            [ls.append(i['id']) for i in activty.values('id')]
            [print(i) for i in ls]
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) < 10:
                print('올레 포함')
                activty = {'activty': random.sample(ls, int(self.days - 1))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty
            if (self.mbti_list[2] == 'e' or self.mbti_list[8] == 't') and int(self.days) >= 10:
                print('10일 이상 올레 포함')
                activty = {'activty': random.sample(ls, int(self.days - olle_days))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty
            else:
                print('올레 비포함')
                activty = {'activty': random.sample(ls, int(self.days))}  # 여러개
                # activty = {'activty': ls[random.randint(0, len(ls) - 1)]}  # 1개
                return activty



    def tourism(self, activty, olle):
        # 액티비티 주변의 2개 추천 생각
        # BUT 이러면, 자기들끼리 중복 가능성 高
        # 랜덤 형성 후, 가까운 것 끼리 집합 형식 생각 필요
        # e, s, t, j = mbti
        activty = Activity.objects.filter(id__in=activty['activty']).values()
        if Olle.objects.filter(name__in=olle['olle']).values() != None:
            olle = Olle.objects.filter(name__in=olle['olle']).values()
            # [(print(i['lat'], i['log'], i['lat'])) for i in activty.values()]
            list = []
            for i in activty.values():
                list.append(Tourism.objects.raw(
                    'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                    '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                    'AS distance FROM tourism WHERE tour_category_id != 8 and 12 ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2])
            for i in olle.values():
                list.append(Tourism.objects.raw(
                    "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                    "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                    "AS distance FROM tourism WHERE tour_category_id != 8 and 12 ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2])
            # print(restaurant)
            # [print(i) for i in list]
            print(list)
            # print(str(restaurant))
            # serializer = RestaurantSerializer(restaurant, many=True)
            # print(serializer.data)

            return list
        else:
            oleum = Tourism.objects.filter(name__in=olle['olle']).values()
            list = []
            for i in activty.values():
                list.append(Tourism.objects.raw(
                    "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                    "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                    "AS distance FROM tourism WHERE tour_category_id != 8, 12 ORDER BY distance",
                    [i['lat'], i['log'], i['lat']])[:2])
            for i in oleum.values():
                list.append(Tourism.objects.raw(
                    "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                    "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                    "AS distance FROM tourism WHERE tour_category_id != 8, 12 ORDER BY distance",
                    [i['lat'], i['log'], i['lat']])[:2])

            print(list)

            return list

        # 계절에 따라 분류, 정리, 겨울에는 오름 제외
        # 올레와 유사하게 오름 추천
        # 날짜가 10일 미만일 경우 0 or 1 랜덤, 10 이상 일 경우, 10% 비율로 적용


    def olle_set(self, mbti):
        e, s, t, j = mbti
        # 날짜가 10일 미만일 경우 0 or 1 랜덤, 10 이상 일 경우, 10% 비율로 적용
        # 올레와 오름을 합쳐서 랜덤 값으로 나가자!
        # 계절에 따라 분류, 정리, 겨울에는 오름 제외
        print(int(self.days * 0.20))
        days = int(self.days * 0.20)
        if self.days < 10 :
            if self.mbti_list[2] == 'e' or self.mbti_list[8] == 't':
                ls, ls2 = [], []
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                # [ls.append(f"olle{i['id']}") for i in olle.values('id')]
                # [ls.append(i) for i in olle.values('id')]  # [{'id': 1}, {'id': 2}, {'id': 3}]
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                print(ls)
                # olle = {'olle': i for i in ls}
                # print(olle)
                # olle = {'olle': random.sample(ls, days)}  #  여러개
                # olle = {'olle': i for i in random.sample(ls, days)}  # dict 형식 변화 -> 마지막 값만 들어감
                olle = {'olle': ls[random.randint(0, len(ls) - 1)] }  # 한개
                return olle
            else:
                return 0
        else:
            if self.mbti_list[2] == 'e' or self.mbti_list[8] == 't':
                ls, ls2 = [], []
                olle = Olle.objects.all()
                oleum = Tourism.objects.filter(tour_category__in=[12, 8]).values()
                # [ls.append(f"olle{i['id']}") for i in olle.values('id')]
                # [ls.append(i) for i in olle.values('id')]  # [{'id': 1}, {'id': 2}, {'id': 3}]
                # [ls.append(f"olle.{i['id']}") for i in olle.values('id')]
                # [ls.append(f"oleum.{i['id']}") for i in oleum.values('id')]
                [ls.append(i['name']) for i in olle.values('name')]
                [ls.append(i['name']) for i in oleum.values('name')]
                print(ls)
                # olle = {'olle': i for i in ls}
                # print(olle)
                olle = {'olle': random.sample(ls, days)}   # 여러개
                # olle = {'olle': i for i in random.sample(ls, days)}  # dict 형식 변화 -> 마지막 값만 들어감
                # olle = {'olle': ls[random.randint(0, len(ls) - 1)] }  # 한개
                return olle
            else:
                return 0


    def restaurant(self, activty, olle):
        # acc = Accommodation.objects.filter(id=acc['acc']).values()[0]
        # print(acc['lat'], acc['log'])
        #
        # restaurant = Restaurant.objects.raw(
        #     'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
        #     '-radians(%s))+sin(radians(%s))*sin(radians(lat)))) '
        #     'AS distance FROM restaurant ORDER BY distance',
        #     [acc['lat'], acc['log'], acc['lat']])[:2]
        # # print(restaurant)
        # [print(i) for i in restaurant]
        # # print(str(restaurant))
        # # serializer = RestaurantSerializer(restaurant, many=True)
        # # print(serializer.data)
        #
        #
        # return restaurant
        activty = Activity.objects.filter(id__in=activty['activty']).values()
        if Olle.objects.filter(name__in=olle['olle']).values() != None:
            olle = Olle.objects.filter(name__in=olle['olle']).values()
            list = []
            for i in activty.values():
                list.append(Restaurant.objects.raw(
                    'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                    '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                    'AS distance FROM restaurant ORDER BY distance',[i['lat'], i['log'], i['lat']])[:2])
            for i in olle.values():
                list.append(Restaurant.objects.raw(
                    "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                    "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                    "AS distance FROM restaurant ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2])

            return list
        else:
            oleum = Tourism.objects.filter(name__in=olle['olle']).values()
            list = []
            for i in activty.values():
                list.append(Restaurant.objects.raw(
                    'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
                    '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
                    'AS distance FROM restaurant ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2])
            for i in oleum.values():
                list.append(Restaurant.objects.raw(
                    "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
                    "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
                    "AS distance FROM restaurant ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2])

            return list
    # def test(self, acc, activty, olle):
    #     dic = {}
    #     activty = Activity.objects.filter(id__in=activty['activty']).values()
    #     if Olle.objects.filter(name__in=olle['olle']).values() != None:
    #         olle = Olle.objects.filter(name__in=olle['olle']).values()
    #         except_id = []
    #         for i in activty.values():
    #
    #             a = Restaurant.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
    #                 '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
    #                 'AS distance FROM restaurant ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2]
    #             b = Tourism.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM tourism ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2]
    #             c = Activity.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
    #             d = Shop.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop HAVING distance < 4 ORDER BY distance',
    #                 [i['lat'], i['log'], i['lat']])[:1]
    #             print(a+b)
    #             print(a['Restaurant'])
    #
    #
    #             # union = set(a) & set(b)
    #             dic[f"day: {i['name']}"] = c+a+b+d
    #             except_id.append()
    #             # dic[i.name] = a.union(b)
    #         for i in olle.values():
    #
    #             a = Restaurant.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
    #                 '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
    #                 'AS distance FROM restaurant ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2]
    #             serializer_a = RestaurantSerializer(a, many=True)
    #             print(serializer_a.data)
    #
    #             b = Tourism.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM tourism ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2]
    #             serializer_b = RestaurantSerializer(a, many=True)
    #             print(serializer_b.data)
    #             c = Olle.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM olle ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
    #             serializer_c = RestaurantSerializer(a, many=True)
    #             print(serializer_c.data)
    #             d = Shop.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop HAVING distance < 4 ORDER BY distance',
    #                 [i['lat'], i['log'], i['lat']])[:1]
    #
    #             dic[f"day: {i['name']}"] = c + a + b + d
    #
    #     else:
    #         oleum = Tourism.objects.filter(name__in=olle['olle']).values()
    #         for i in activty.values():
    #             a = Restaurant.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
    #                 '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
    #                 'AS distance FROM restaurant ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2]
    #             b = Tourism.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM tourism WHERE tour_category_id != 8, 12 ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2]
    #             c = Activity.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM activity ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
    #             d = Shop.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop HAVING distance < 4 ORDER BY distance',
    #                 [i['lat'], i['log'], i['lat']])[:1]
    #
    #             print(a['Restaurant'])
    #             dic[f"day: {i['name']}"] = c + a + b + d
    #         for i in oleum.values():
    #             a = Restaurant.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)'
    #                 '-radians(%s))+sin(radians(%s))*sin(radians(lat))))'
    #                 'AS distance FROM restaurant ORDER BY distance', [i['lat'], i['log'], i['lat']])[:2]
    #             b = Tourism.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM tourism WHERE tour_category_id != 8, 12 ORDER BY distance", [i['lat'], i['log'], i['lat']])[:2]
    #             c = Tourism.objects.raw(
    #                 "SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)"
    #                 "-radians(%s))+sin(radians(%s))*sin(radians(lat))))"
    #                 "AS distance FROM olle WHERE tour_category_id = 8, 12 ORDER BY distance", [i['lat'], i['log'], i['lat']])[:1]
    #             d = Shop.objects.raw(
    #                 'SELECT *, (6371*acos(cos(radians(%s))*cos(radians(lat))*cos(radians(log)-radians(%s))+sin(radians(%s))*sin(radians(lat)))) AS distance FROM shop HAVING distance < 4 ORDER BY distance',
    #                 [i['lat'], i['log'], i['lat']])[:1]
    #             dic[f"day: {i['name']}"] = c + a + b + d
    #
    #     return dic

    def shop(self):
        pass




if __name__ == '__main__':
    option = {"date1": '2021-05-30', "date2": '2021-06-09', 'start': 'gmp', 'Number': 4, 'user': 2, 'relationship': 'family'}
    a = JejuProcessTest(option)
    # a.process()
    acc = {'acc' : 15}
    activty = {'activty' : [1, 5, 6, 20, 15, 17, 18]}
    # olle = {'olle' : ['용수-저지 올레', '거문오름']}
    olle = {'olle': ['거문오름']}
    a.process_days(acc, activty, olle)


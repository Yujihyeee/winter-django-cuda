from django.db import models

# Create your models here.
from image.models import Image, Category

class TourismCategory(models.Model):

    # TourismCategory
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.TextField()

    class Meta:
        db_table = "category_tourism"

    def __str__(self):
        return f'{self.id}'


class Tourism(models.Model):

    # Tourism
    name = models.TextField()
    address = models.TextField()
    explanation = models.TextField(null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도
    tour_category = models.ForeignKey(TourismCategory, on_delete=models.CASCADE, null=True)  # category
    # tour_business_close_time = models.TimeField(null=True)

    class Meta:
        db_table = "tourism"

    def __str__(self):
        return f'{self.id}'

class ActivityCategory(models.Model):

    # ActivityCategory
    section = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.TextField()  # section
    type = models.TextField()  # category

    class Meta:
        db_table = "category_activity"

    def __str__(self):
        return f'{self.id}'

class Activity(models.Model):
    currencies = [
        ('W', "Korean Won (W)"),
    ]

    # Activity
    name = models.TextField()  # name
    start_business_time = models.TimeField()  # start time
    end_business_time = models.TimeField()  # end time
    time = models.TimeField()  # time
    contact = models.TextField()  # contact
    loc = models.TextField()  # location
    price = models.IntegerField(choices=currencies, default="$")  # expense
    act_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE, null=True)  # category
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도

    class Meta:
        db_table = "activity"

    def __str__(self):
        return f'{self.id}'

class PlaneCategory(models.Model):

    # PlaneCategory
    section = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    category = models.TextField()  # type
    type = models.TextField()  # depAirportNm,arrAirportNm

    class Meta:
        db_table = "category_plane"

    def __str__(self):
        return f'{self.id}'

class Plane(models.Model):
    currencies = [
        ('W', "Korean Won (W)"),
    ]
    #  Plane # api활용 (https://www.data.go.kr/data/15000755/openapi.do)
    plane_category = models.ForeignKey(PlaneCategory, on_delete=models.CASCADE, null=True)
    vihicleId = models.TextField()   # 항공편명
    airlineNm = models.TextField()   # 항공사명
    depPlandTime = models.TimeField()   # 출발시간
    arrPlandTime = models.TimeField()   # 도착시간
    economyCharge = models.IntegerField(choices=currencies, default="$")   # 일반석운임
    # depAirportNm = models.TextField()  # 출발공항
    # arrAirportNm = models.TextField()  # 도착공항

    class Meta:
        db_table = "plane"

    def __str__(self):
        return f'{self.id}'

# class ShopCategory(models.Model):
#
#     # RestaurantCategory
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
#     type = models.TextField()
#
#     class Meta:
#         db_table = "category_shop"
#
#     def __str__(self):
#         return f'{self.id}'


class Shop(models.Model):

    # Shop
    name = models.TextField()
    # business_time = models.TimeField()
    loc = models.TextField()
    explanation = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    recommend = models.TextField()  # 대상자
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도

    class Meta:
        db_table = "shop"

    def __str__(self):
        return f'{self.id}'



class RestaurantCategory(models.Model):

    # RestaurantCategory
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.TextField()

    class Meta:
        db_table = "category_restaurant"

    def __str__(self):
        return f'{self.id}'


class Restaurant(models.Model):

    # Restaurant
    name = models.TextField()
    res_category = models.ForeignKey(RestaurantCategory, on_delete=models.CASCADE, null=True)
    loc = models.TextField()  # address
    recommend = models.TextField()  # food
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)  # photo
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도

    class Meta:
        db_table = "restaurant"

    def __str__(self):
        return f'{self.id}'


class AccommodationCategory(models.Model):

    # AccommodationCategory
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    type = models.TextField()

    class Meta:
        db_table = "category_accommodation"

    def __str__(self):
        return f'{self.id}'


class Accommodation(models.Model):
    currencies = [
        ('W', "Korean Won (W)"),
    ]

    # Accommodation
    name = models.TextField()  # 상호명
    loc = models.TextField()  # 소재지
    acc_category = models.ForeignKey(AccommodationCategory, on_delete=models.CASCADE, null=True)  # 구분
    price = models.IntegerField(choices=currencies, default="$")  # 1박당가격
    contact = models.TextField()  # 연락처
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    standard_number = models.IntegerField()  # 숙박인원
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도

    class Meta:
        db_table = "accommodation"

    def __str__(self):
        return f'{self.id}'

class Olle(models.Model):

    # Olle
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    course = models.TextField()
    name = models.TextField()  # course-name
    distance = models.FloatField()
    time = models.TimeField()
    starting_point = models.TextField()
    end_point = models.TextField()
    explanation = models.TextField()
    lat = models.FloatField(null=True)  # 위도
    log = models.FloatField(null=True)  # 경도
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "olle"

    def __str__(self):
        return f'{self.id}'



# # class Jeju(models.Model):
# #
# #     # #  Plane
# #     # plane_airline = models.TextField()
# #     # plane_date = models.DateField()
# #     # plane_departure_time = models.TimeField()
# #     # plane_departures = models.TextField()
# #     # plane_arrivals = models.TextField()
# #     # plane_price = models.IntegerField()
# #     # plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
# #
# #     # # Shop
# #     # shop_name = models.TextField()
# #     # shop_business_time = models.TimeField()
# #     # shop_loc = models.TextField()
# #     shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
# #
# #     # # Restaurant
# #     # res_name = models.TextField()
# #     # res_business_time = models.TimeField()
# #     # res_loc = models.TextField()
# #     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
# #
# #     # # Tourism
# #     # tour_name = models.TextField()
# #     # tour_loc = models.TextField()
# #     # tour_type = models.IntegerField()
# #     # tour_business_time = models.TimeField()
# #     tourism = models.ForeignKey(Tourism, on_delete=models.CASCADE, null=True)
# #
# #     # # Activity
# #     # act_name = models.TextField()
# #     # act_business_time = models.TimeField()
# #     # act_loc = models.TextField()
# #     # act_price = models.IntegerField()
# #     activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
# #
# #     # # Accommodation
# #     # acc_name = models.TextField()
# #     # acc_loc = models.TextField()
# #     # acc_price = models.IntegerField()
# #     # acc_type = models.IntegerField()
# #     accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=True)
# #
# #
# #
# #     class Meta:
# #         db_table = "jeju_data"
# #
# #     def __str__(self):
# #         return f'{self.id}'
from datetime import datetime
from random import random
from django.db import models
# Create your models here.
from icecream import ic
from django.db.models import IntegerField, CharField
from django_mysql.models import ListCharField, ListTextField
from image.models import Category
from jeju_data.models import Accommodation
from user.models import User


class JejuSchedule(models.Model):
    # days[0], plane, acc, activity, olle, restaurant, tourism, shop, startday, endday, day, people, user, relationship
    # Jeju_Schedule
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user
    reg_date = models.DateTimeField(default=datetime.now())  # 생성일
    startday = models.DateField()  # startday
    endday = models.DateField()  # endday
    day = models.IntegerField()  # day
    startloc = models.TextField()  # startloc
    people = models.IntegerField()  # people
    relationship = models.TextField()  # relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # recommend
    plane = ListTextField(base_field=CharField(max_length=255), size=5)  # plane
    acc = models.ForeignKey(Accommodation, max_length=255, on_delete=models.CASCADE)  # acc
    activity = ListTextField(base_field=CharField(max_length=255), size=50, null=True)  # activity
    olle = ListTextField(base_field=CharField(max_length=255), size=50, null=True)  # olle
    restaurant = ListTextField(base_field=CharField(max_length=255), size=100, null=True)  # restaurant
    tourism = ListTextField(base_field=CharField(max_length=255), size=100, null=True)  # tourism
    shop = ListTextField(base_field=CharField(max_length=255), size=50, null=True)  # shop
    schedule = ListTextField(base_field=CharField(max_length=255), size=50, null=True)  # days[0]

    class Meta:
        db_table = "jeju_schedule"

    def __str__(self):
        return f'{self.id}'

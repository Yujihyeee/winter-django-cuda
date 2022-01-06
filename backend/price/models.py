from django.db import models
from django.db.models import IntegerField
from django_mysql.models import ListCharField


class Price(models.Model):
    category_id = models.IntegerField()
    name = models.TextField()
    category = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'price'

    def __str__(self):
        return f'[{self.pk}] {self.id}'


class Pay(models.Model):
    re_id = models.IntegerField(primary_key=True)
    reg_date = models.DateField()
    user = models.IntegerField()
    day = models.IntegerField()
    people = models.IntegerField()
    plane = ListCharField(base_field=IntegerField(), size=50, null=True, max_length=100)
    acc = models.IntegerField()
    activity = ListCharField(base_field=IntegerField(), size=50, null=True, max_length=100)

    class Meta:
        db_table = "pay"

    def __str__(self):
        return f'[{self.pk}]'

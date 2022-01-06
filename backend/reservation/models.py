from django.db import models
from price.models import Price


class Reservation(models.Model):
    reg_date = models.DateField()
    people = models.IntegerField()
    day = models.IntegerField()
    plane_unit = models.IntegerField()
    plane_price = models.IntegerField()
    acc_unit = models.IntegerField()
    acc_price = models.IntegerField()
    act_unit = models.IntegerField()
    act_price = models.IntegerField()
    price = models.IntegerField()
    tax = models.IntegerField()
    subtotal = models.IntegerField()
    fees = models.IntegerField()
    total_price = models.IntegerField()
    jeju_schedule = models.IntegerField()
    user = models.IntegerField()

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

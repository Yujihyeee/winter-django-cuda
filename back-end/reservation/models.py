from django.db import models

from brevity.models import Brevity


class Reservation(models.Model):
    subtotal = models.IntegerField()
    fees = models.IntegerField()
    total_price = models.IntegerField()
    brevity = models.ForeignKey(Brevity, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

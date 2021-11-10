from django.db import models

# Create your models here.


class Reservation(models.Model):
    schedule = models.TextField()
    voucher = models.TextField()
    caution = models.TextField()
    fees = models.IntegerField()
    client = models.TextField()

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

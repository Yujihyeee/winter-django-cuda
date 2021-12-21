from django.db import models
from jeju_schedule.models import JejuSchedule
from reservation.models import Reservation


class Ledger(models.Model):
    date = models.DateField()
    category = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'ledger'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'날짜: {self.date}' \
               f'항목명: {self.category}' \
               f'금액: {self.price}'

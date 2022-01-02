from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from reservation.models import Reservation


class Ledger(models.Model):
    year = models.IntegerField()
    date = models.DateField()
    category = models.TextField()
    price = models.BigIntegerField([MinValueValidator(1), MaxValueValidator(100)])

    class Meta:
        db_table = 'ledger'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'년도: {self.year}' \
               f'날짜: {self.date}' \
               f'항목명: {self.category}' \
               f'금액: {self.price}'

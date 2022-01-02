from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ledger.models import Ledger


class FinReports(models.Model):
    year = models.IntegerField()
    category = models.TextField()
    price = models.BigIntegerField([MinValueValidator(1), MaxValueValidator(100)])
    ledger = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'fin_reports'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'연도: {self.year}' \
               f'항목명: {self.category}' \
               f'금액: {self.price}' \
               f'{self.ledger_id}'

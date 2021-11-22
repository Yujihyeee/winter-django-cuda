from django.db import models


class FinReports(models.Model):
    year = models.IntegerField()
    category = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'fin_reports'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

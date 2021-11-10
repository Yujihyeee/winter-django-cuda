from django.db import models

# Create your models here.


class FinReports(models.Model):
    factory = models.TextField()
    category = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'fin_reports'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

from django.db import models


class Price(models.Model):
    category_id = models.IntegerField()
    name = models.TextField()
    category = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'price'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

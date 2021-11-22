from django.db import models


class Brevity(models.Model):
    userid = models.IntegerField()
    plane = models.TextField()
    accommodation = models.TextField()
    activity = models.TextField(null=True)
    restaurant = models.TextField(null=True)
    shop = models.TextField(null=True)
    tourism = models.TextField(null=True)
    olle = models.TextField(null=True)
    option = models.TextField()

    class Meta:
        db_table = 'brevity'

    def __str__(self):
        return f'[{self.pk}] {self.id}'

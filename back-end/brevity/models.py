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
        return f'[{self.pk}] {self.id}' \
               f'회원명: {self.userid}' \
               f'항공편: {self.plane}' \
               f'숙소: {self.accommodation}' \
               f'액티비티: {self.activity}' \
               f'식당: {self.restaurant}' \
               f'쇼핑: {self.shop}' \
               f'투어: {self.tourism}' \
               f'올레길: {self.olle}' \
               f'옵션: {self.option}'

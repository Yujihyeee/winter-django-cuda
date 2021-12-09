from django.db import models
from image.models import Category, Image


class Person(models.Model):
    # use_in_migrations = True
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    age = models.IntegerField()
    gender = models.BooleanField()
    mbti = models.TextField()

    class Meta:
        db_table = "person"

    def __str__(self):
        return f'[{self.pk}]'


class User(models.Model):
    # use_in_migrations = True
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    name = models.TextField()
    email = models.EmailField()
    birth = models.DateField()
    gender = models.TextField()
    mbti = models.TextField()
    mbti_list = models.TextField()
    card_number = models.TextField()
    card_company = models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    person_category = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk}'

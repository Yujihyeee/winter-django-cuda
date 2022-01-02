from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    address = models.TextField()
    birth = models.DateField()
    card_company = models.TextField()
    card_number = models.BigIntegerField([MinValueValidator(1), MaxValueValidator(100)])
    email = models.TextField()
    first_name = models.TextField()
    gender = models.TextField()
    last_name = models.TextField()
    mbti = models.TextField()
    mbti_list = models.TextField()
    name = models.TextField()
    passport = models.TextField()
    password = models.TextField()
    phone_number = models.TextField()
    reg_date = models.TextField()
    username = models.TextField()

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'[{self.pk}] '

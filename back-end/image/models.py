# from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CharField, TextField
from django_mysql.models import ListTextField

# Create your models here.


class Category(models.Model):

    # Category
    section = models.TextField()
    category = models.TextField()

    class Meta:
        db_table = "category"

    def __str__(self):
        return f'{self.id}'


class Image(models.Model):

    # Image
    name = models.TextField()
    url = ListTextField(base_field=CharField(max_length=255), size=6)
    # url = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "image"

    def __str__(self):
        return f'{self.id}'

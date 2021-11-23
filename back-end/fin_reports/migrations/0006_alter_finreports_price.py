# Generated by Django 3.2.9 on 2021-11-23 02:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fin_reports', '0005_alter_finreports_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finreports',
            name='price',
            field=models.BigIntegerField(verbose_name=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]

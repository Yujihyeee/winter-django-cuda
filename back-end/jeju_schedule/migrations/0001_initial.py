# Generated by Django 3.2.5 on 2021-12-16 09:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jeju_data', '0001_initial'),
        ('image', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JejuSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateTimeField(default=datetime.datetime(2021, 12, 16, 18, 31, 33, 551885))),
                ('startday', models.DateField()),
                ('endday', models.DateField()),
                ('day', models.IntegerField()),
                ('startloc', models.TextField()),
                ('people', models.IntegerField()),
                ('relationship', models.TextField()),
                ('plane', django_mysql.models.ListTextField(models.CharField(max_length=255), size=5)),
                ('activity', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=50)),
                ('olle', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=50)),
                ('restaurant', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=100)),
                ('tourism', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=100)),
                ('shop', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=50)),
                ('schedule', django_mysql.models.ListTextField(models.CharField(max_length=255), null=True, size=50)),
                ('acc', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='jeju_data.accommodation')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'jeju_schedule',
            },
        ),
    ]
from django.db import models
from jeju_schedule.models import JejuSchedule


class Reservation(models.Model):
    reg_date = models.DateField()
    people = models.IntegerField()
    day = models.IntegerField()
    plane_pr = models.IntegerField()
    acc_pr = models.IntegerField()
    act_pr = models.IntegerField()
    price = models.IntegerField()
    tax = models.IntegerField()
    subtotal = models.IntegerField()
    fees = models.IntegerField()
    total_price = models.IntegerField()
    jeju_schedule = models.ForeignKey(JejuSchedule, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reservation'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'인원수: {self.people}' \
               f'숙박일: {self.day}' \
               f'항공권: {self.plane_pr}' \
               f'숙소: {self.acc_pr}' \
               f'액티비티: {self.act_pr}' \
               f'결제내역: {self.price}' \
               f'부가가치세: {self.tax}' \
               f'수수료 붙기 전 총금액: {self.subtotal}' \
               f'여행수수료: {self.fees}' \
               f'총금액: {self.total_price}'

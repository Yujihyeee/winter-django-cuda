from django.db import models
from jeju_schedule.models import JejuSchedule
from reservation.models import Reservation


class Ledger:
    reg_date = models.ForeignKey(JejuSchedule, on_delete=models.CASCADE)
    category = models.TextField()
    price = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ledger'

    def __str__(self):
        return f'[{self.pk}] {self.id}' \
               f'날짜: {self.reg_date}' \
               f'항목명: {self.category}' \
               f'금액: {self.price}'

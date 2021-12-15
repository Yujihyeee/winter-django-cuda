from django.db import models
from reservation.models import Reservation


class Ledger:
    pay = models.IntegerField()  # 급여
    welfare_benefit = models.IntegerField()  # 복리후생비
    advertising_expense = models.IntegerField()  # 광고선전비
    car_maintenance_fee = models.IntegerField()  # 차량유지비
    depreciation_fee = models.IntegerField()  # 감가상각비
    commission_fee = models.IntegerField()  # 지급수수료
    reg_date = models.ForeignKey(Reservation, on_delete=models.CASCADE)  # 날짜

    class Meta:
        db_table = 'ledger'

    def __str__(self):
        return f'[{self.pk}] {self.reg_date}' \
               f'{self.pay}' \
               f'{self.welfare_benefit}' \
               f'{self.advertising_expense}' \
               f'{self.car_maintenance_fee}' \
               f'{self.depreciation_fee}' \
               f'{self.commission_fee}'

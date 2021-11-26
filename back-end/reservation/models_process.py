# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가
from django.db.models import Sum
import brevity
from common.models import ValueObject, Reader, Printer


class Processing:
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        self.csvfile = reader.new_file(vo)

    def process(self):
        price = brevity.objects.filter(category=3).aggregate(Sum('',))
        tax = price * 0.1
        subtotal = price + tax
        fees = subtotal * 0.2
        total_price = subtotal + fees

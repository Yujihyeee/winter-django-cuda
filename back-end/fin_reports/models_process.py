from common.models import ValueObject, Reader, Printer
from fin_reports.models import FinReports
from ledger.models import Ledger


class ReportProcessing:
    def __init__(self, option):
        self.reg_date = FinReports.objects.filter()
        self.category = option['매출액', '매출원가', '판매비와관리비', '영업이익', '기타손익 및 금융손익',
                               '기타수익', '기타비용', '금융수익', '금융비용', '당기순이익']
        self.price = FinReports.objects.filter()

    def process(self):
        for row in data_reader:
            ledger = Ledger.objects.update(date=row['date'],
                                           category=row['category'],
                                           price=row['price'])
            print(f'2 >>>> {ledger}')

        print('DATA UPLOADED SUCCESSFULLY!')

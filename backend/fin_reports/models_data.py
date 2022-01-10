from common.models import ValueObject, Printer, Reader
from fin_reports.models import FinReports
from ledger.models import Ledger
from ledger.serializer import LedgerSerializer


class DbUploader:

    def insert_data(self):
        self.insert_fin_report()

    def insert_fin_report(self):
        ledger = Ledger.objects.filter(year=2020)
        ledger = LedgerSerializer(ledger, many=True).data
        for row in ledger:
            print(row)
            fin_reports = FinReports.objects.create(year=row['year'],
                                                    category=row['category'],
                                                    price=row['price'],
                                                    ledger_id=row['id']
                                                    )
            print(f'1 >>>> {fin_reports}')
        print('USER DATA UPLOADED SUCCESSFULLY!')

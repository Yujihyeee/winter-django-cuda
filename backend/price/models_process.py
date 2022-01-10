import csv
from price.models import Price


class Processing:

    def price_process(self):
        with open('price/data/plane.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['vihicleId'],
                                             category='plane',
                                             price=row['economyCharge']
                                             )
                print(f'2 >>>> {price}')

        with open('price/data/accommodation.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['name'],
                                             category='accommodation',
                                             price=row['1박당가격']
                                             )
                print(f'2 >>>> {price}')

        with open('price/data/activity.csv', newline='', encoding='utf8') as f:
            data_reader = csv.DictReader(f)
            for row in data_reader:
                price = Price.objects.create(category_id=row['id'],
                                             name=row['name'],
                                             category='activity',
                                             price=row['expense']
                                             )
                print(f'2 >>>> {price}')

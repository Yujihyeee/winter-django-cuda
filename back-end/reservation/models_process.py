# 여행업 알선 수입＝여행자로부터 받는 관광요금－원가

class Processing:
    def __init__(self):
        pass

    def process(self):
        price = 0
        tax = price * 0.1
        subtotal = price + tax
        fees = subtotal * 0.2
        total_price = subtotal + fees

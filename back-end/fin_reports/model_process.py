

class Processing:
    def __init__(self):
        pass

    def process(self):
        price = 0
        qty = 0
        tax = price * qty * 0.1
        subtotal = price * qty + tax
        fee = subtotal * 0.2
        total = subtotal + fee

class Wallet:
    def __init__(self, amount):
        self.__amount = amount  # private

    def get_amount(self):
        return self.__amount

@register
def demo_11():
    w = Wallet(500)
    print("11: amount via getter =", w.get_amount())

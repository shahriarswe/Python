class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} via credit card"

@register
def demo_27():
    print("27:", CreditCard().pay(100))


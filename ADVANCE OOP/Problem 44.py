class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

class BankAccount44:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

@register
def demo_44():
    acc = BankAccount44(100)
    try:
        acc.withdraw(500)
    except InsufficientFundsError as e:
        print("44:", e)
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Cannot withdraw {amount}, balance is only {balance}")

class BankAccount44:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

@register
def demo_44():
    acc = BankAccount44(100)
    try:
        acc.withdraw(500)
    except InsufficientFundsError as e:
        print("44:", e)

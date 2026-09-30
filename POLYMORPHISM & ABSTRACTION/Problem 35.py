class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

@register
def demo_35():
    m1, m2 = Money(50), Money(80)
    print("35: m1 == m2?", m1 == m2, "| m1 < m2?", m1 < m2)


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato", "basil"])

@register
def demo_09():
    p = Pizza.margherita()
    print("09: margherita toppings =", p.toppings)

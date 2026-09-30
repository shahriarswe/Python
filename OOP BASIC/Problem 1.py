class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"{self.brand} {self.model}"

@register
def demo_01():
    c = Car("Toyota", "Corolla")
    print("01:", c.describe())

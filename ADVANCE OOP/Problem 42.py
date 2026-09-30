class Employee42:
    raise_percent = 1.05

    def __init__(self, salary):
        self.salary = salary

    def apply_raise(self):
        self.salary *= Employee42.raise_percent

    @classmethod
    def set_raise_percent(cls, percent):
        cls.raise_percent = percent

@register
def demo_42():
    e = Employee42(1000)
    Employee42.set_raise_percent(1.10)
    e.apply_raise()
    print("42: new salary =", round(e.salary, 2))

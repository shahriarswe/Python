class Person14:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

@register
def demo_14():
    p = Person14(25)
    p.age = 30
    print("14: updated age =", p.age)

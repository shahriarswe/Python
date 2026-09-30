class Person22:
    def __init__(self, name):
        self.name = name

class Employee22(Person22):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

@register
def demo_22():
    e = Employee22("Tanvir", 40000)
    print("22:", e.name, e.salary)

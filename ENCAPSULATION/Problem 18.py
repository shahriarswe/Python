class Employee18:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

@register
def demo_18():
    e = Employee18("Karim", 50000)
    print("18: salary =", e.get_salary())

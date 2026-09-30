class Employee37(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

    def describe(self):
        return f"{self.name} earns {self.calculate_pay()}"

class Manager37(Employee37):
    def calculate_pay(self):
        return 8000

@register
def demo_37():
    m = Manager37("Fatima")
    print("37:", m.describe())

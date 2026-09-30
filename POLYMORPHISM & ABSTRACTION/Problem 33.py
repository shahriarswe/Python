class Shape33(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle33(Shape33):
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height

@register
def demo_33():
    t = Triangle33(6, 4)
    print("33: triangle area =", t.area())

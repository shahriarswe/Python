class Shape50(ABC):
    def __init__(self, name):
        self.__name = name  # encapsulated

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def area(self):
        pass

    def summary(self):
        return f"{self.name}: area = {round(self.area(), 2)}"

class Circle50(Shape50):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle50(Shape50):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width, self.height = width, height

    def area(self):
        return self.width * self.height

@register
def demo_50():
    shapes = [Circle50(3), Rectangle50(4, 5)]
    for s in shapes:
        print("50:", s.summary())


if __name__ == "__main__":
    for demo in demos:
        demo()

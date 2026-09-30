class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

@register
def demo_03():
    r1, r2 = Rectangle(4, 5), Rectangle()
    print("03: area r1 =", r1.area(), "| area r2 (default) =", r2.area())

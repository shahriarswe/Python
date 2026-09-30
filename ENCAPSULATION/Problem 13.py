class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

@register
def demo_13():
    c = Circle(3)
    print("13: circle area =", round(c.area, 2))

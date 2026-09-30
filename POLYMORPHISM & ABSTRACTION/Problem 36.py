class Circle36:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

class Square36:
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

@register
def demo_36():
    shapes = [Circle36(2), Square36(3)]
    for s in shapes:
        print("36:", type(s).__name__, "area =", round(s.area(), 2))

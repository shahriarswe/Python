class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

@register
def demo_34():
    v1, v2 = Vector(1, 2), Vector(3, 4)
    print("34:", v1 + v2)

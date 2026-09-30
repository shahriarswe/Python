class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"

@register
def demo_04():
    p = Point(3, 4)
    print("04: str =", str(p), "| repr =", repr(p))

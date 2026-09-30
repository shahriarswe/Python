class Shape25:
    def info(self):
        return "This is a shape"

class Square25(Shape25):
    def info(self):
        base = super().info()
        return base + ", specifically a square"

@register
def demo_25():
    print("25:", Square25().info())


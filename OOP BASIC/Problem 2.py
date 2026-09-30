class Counter:
    total_created = 0  # class variable, shared by all instances

    def __init__(self):
        self.id = Counter.total_created  # instance variable
        Counter.total_created += 1

@register
def demo_02():
    a, b, c = Counter(), Counter(), Counter()
    print("02: ids =", a.id, b.id, c.id, "| total created =", Counter.total_created)

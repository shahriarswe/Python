class A28:
    def __init__(self):
        self.a = "A"

class B28(A28):
    def __init__(self):
        super().__init__()
        self.b = "B"

class C28(B28):
    def __init__(self):
        super().__init__()
        self.c = "C"

@register
def demo_28():
    obj = C28()
    print("28:", obj.a, obj.b, obj.c)

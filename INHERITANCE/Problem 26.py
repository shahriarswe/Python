class Base26:
    def greet(self):
        return "Base"

class Left26(Base26):
    def greet(self):
        return "Left"

class Right26(Base26):
    def greet(self):
        return "Right"

class Bottom26(Left26, Right26):
    pass

@register
def demo_26():
    print("26: greet() resolves to ->", Bottom26().greet(), "| MRO:",
          [c.__name__ for c in Bottom26.__mro__])

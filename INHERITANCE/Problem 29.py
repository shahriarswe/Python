class Vehicle29:
    pass

class Car29(Vehicle29):
    pass

@register
def demo_29():
    c = Car29()
    print("29: isinstance(c, Vehicle29) =", isinstance(c, Vehicle29),
          "| issubclass(Car29, Vehicle29) =", issubclass(Car29, Vehicle29))


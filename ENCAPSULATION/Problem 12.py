class Vehicle12:
    def __init__(self, speed):
        self._speed = speed  # protected by convention

class Bike(Vehicle12):
    def show_speed(self):
        return self._speed

@register
def demo_12():
    b = Bike(40)
    print("12: bike speed =", b.show_speed())

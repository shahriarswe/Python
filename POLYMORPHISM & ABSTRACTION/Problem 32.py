class Duck32:
    def sound(self):
        return "Quack"

class Robot32:
    def sound(self):
        return "Beep"

@register
def demo_32():
    for thing in [Duck32(), Robot32()]:
        print("32:", thing.sound())

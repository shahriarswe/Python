class Cat31:
    def speak(self):
        return "Meow"

class Cow31:
    def speak(self):
        return "Moo"

@register
def demo_31():
    for animal in [Cat31(), Cow31()]:
        print("31:", type(animal).__name__, "says", animal.speak())

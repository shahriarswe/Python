class Animal21:
    def speak(self):
        return "..."

class Dog21(Animal21):
    def speak(self):
        return "Woof!"

@register
def demo_21():
    print("21:", Dog21().speak())

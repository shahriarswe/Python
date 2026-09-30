class Dog49:
    def speak(self):
        return "Woof"

class Cat49:
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def create_animal(kind):
        animals = {"dog": Dog49, "cat": Cat49}
        if kind not in animals:
            raise ValueError(f"Unknown animal type: {kind}")
        return animals[kind]()

@register
def demo_49():
    a = AnimalFactory.create_animal("cat")
    print("49:", a.speak())

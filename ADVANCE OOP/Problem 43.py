class Engine:
    def start(self):
        return "Engine started"

class Car43:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        return self.engine.start() + ", car is ready to drive"

@register
def demo_43():
    print("43:", Car43().start())

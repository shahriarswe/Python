class LivingThing:
    def breathe(self):
        return "breathing"

class Animal23(LivingThing):
    def move(self):
        return "moving"

class Human23(Animal23):
    def think(self):
        return "thinking"

@register
def demo_23():
    h = Human23()
    print("23:", h.breathe(), "|", h.move(), "|", h.think())



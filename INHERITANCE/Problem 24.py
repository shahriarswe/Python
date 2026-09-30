class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck24(Flyer, Swimmer):
    pass

@register
def demo_24():
    d = Duck24()
    print("24:", d.fly(), "&", d.swim())

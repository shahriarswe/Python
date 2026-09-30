class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class Product48(JSONMixin):
    def __init__(self, name, price):
        self.name, self.price = name, price

@register
def demo_48():
    p = Product48("Keyboard", 25)
    print("48:", p.to_json())

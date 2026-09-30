class TextBuilder:
    def __init__(self):
        self.text = ""

    def add(self, word):
        self.text += word + " "
        return self  # enables method chaining

@register
def demo_08():
    result = TextBuilder().add("Hello").add("OOP").add("World").text.strip()
    print("08:", result)

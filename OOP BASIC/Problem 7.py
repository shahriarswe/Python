class TempFile:
    def __init__(self, name):
        self.name = name
        print(f"07: opened resource '{self.name}'")

    def __del__(self):
        print(f"07: closed resource '{self.name}'")

@register
def demo_07():
    t = TempFile("session.log")
    del t  # forces __del__ deterministically for this demo

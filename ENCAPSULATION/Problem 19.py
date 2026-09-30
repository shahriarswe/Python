class Secret:
    def __init__(self):
        self.__code = "1234"

@register
def demo_19():
    s = Secret()
    print("19: accessed via mangled name =", s._Secret__code)

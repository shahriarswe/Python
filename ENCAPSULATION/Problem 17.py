class Stack17:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop() if self.__items else None

    def is_empty(self):
        return len(self.__items) == 0

@register
def demo_17():
    s = Stack17()
    s.push(1)
    s.push(2)
    print("17: popped =", s.pop(), "| empty now?", s.is_empty())

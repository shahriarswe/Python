class Animal10:
    pass

@register
def demo_10():
    a, b = Animal10(), Animal10()
    print("10: same class?", type(a) == type(b), "| same object?", a is b)


if __name__ == "__main__":
    for demo in demos:
        demo()

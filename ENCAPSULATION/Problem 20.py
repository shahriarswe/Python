class FullName:
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    @property
    def full(self):
        return f"{self.__first} {self.__last}"

@register
def demo_20():
    n = FullName("Nusrat", "Jahan")
    print("20: full name =", n.full)


if __name__ == "__main__":
    for demo in demos:
        demo()

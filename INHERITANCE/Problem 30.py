class LoudList(list):
    def append(self, item):
        print(f"30: adding {item!r} to the list")
        super().append(item)

@register
def demo_30():
    ll = LoudList()
    ll.append("apple")
    ll.append("banana")
    print("30: final list =", ll)


if __name__ == "__main__":
    for demo in demos:
        demo()

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

@register
def demo_40():
    try:
        Instrument()
    except TypeError as e:
        print("40: cannot instantiate ABC ->", e)


if __name__ == "__main__":
    for demo in demos:
        demo()

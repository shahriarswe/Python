class SingletonConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

@register
def demo_45():
    a, b = SingletonConfig(), SingletonConfig()
    print("45: same instance?", a is b)

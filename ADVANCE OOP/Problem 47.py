class ManagedResource:
    def __enter__(self):
        print("47: resource acquired")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("47: resource released")
        return False

@register
def demo_47():
    with ManagedResource():
        print("47: using resource")

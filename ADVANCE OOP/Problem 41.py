class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

@register
def demo_41():
    print("41: is_even(10) =", MathUtils.is_even(10))

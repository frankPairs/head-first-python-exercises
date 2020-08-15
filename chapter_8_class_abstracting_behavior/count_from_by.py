class CountFromBy:
    def __init__(self, val: int = 0, inc: int = 1):
        self.val = val
        self.inc = inc

    def __repr__(self) -> str:
        return str(self.val)

    def increase(self):
        self.val += self.inc

    def decrease(self):
        self.val -= self.inc


def main():
    count = CountFromBy(50, 2)

    count.increase()
    count.increase()
    count.decrease()

    print(count)


main()

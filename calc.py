def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("ділення на нуль")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", sub(7, 4))
    print("6 * 5 =", mul(6, 5))
    print("8 / 2 =", div(8, 2))

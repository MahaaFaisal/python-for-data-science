
def square(x: int | float) -> int | float:
    return x**2


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner


def show_cell_content(closure):
    for i in range(len(closure)):
        print(f"closure {i}: {closure[i].cell_contents}")

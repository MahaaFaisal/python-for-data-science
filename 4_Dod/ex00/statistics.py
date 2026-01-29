from math import sqrt


def ft_mean(args: int | float) -> float:
    return sum(args) / len(args)


def ft_var(args: int | float, mean: float) -> float:
    args = tuple(((x - mean)**2 for x in args))
    return sum(args) / len(args)


def ft_std(var: float) -> float:
    return sqrt(var)


def assert_types(args: tuple[int | float], kwargs: dict[str]) -> None:
    assert all(isinstance(x, (int, float)) for x in args)
    assert all(isinstance(x, str) for x in kwargs.values())


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    try:
        assert_types(args, kwargs)
        mean = ft_mean(args)
        print(f"mean: {mean}")
        var = ft_var(args, mean)
        print(f"var: {var}")
        std = ft_std(var)
        print(f"std: {std}")

    except Exception:
        print("ERROR")


ft_statistics(1, 42, 360, 11, 64, toto=4, tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")

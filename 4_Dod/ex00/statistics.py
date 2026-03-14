from math import sqrt


def ft_mean(args: int | float) -> float:
    return sum(args) / len(args)


def ft_var(args: int | float, mean: float) -> float:
    args = tuple(((x - mean)**2 for x in args))
    return sum(args) / len(args)


def ft_std(var: float) -> float:
    return sqrt(var)

def ft_median(args: int | float) -> float:
    n = len(args)
    mid_index = n // 2
    if (mid_index % 2 == 1):
        return (args[mid_index] + args[mid_index + 1]) / 2
    return args[mid_index]

def ft_interquartile(args: int | float) -> float:
    n = len(args)
    i1 = ((25 / 100) * (n))
    print(i1, int(i1))
    i3 = ((75 / 100) * (n))
    print(i3, int(i3))

    return args[int(i1)], args[int(i3)]

def assert_types(args: tuple[int | float], kwargs: dict[str]) -> None:
    assert all(isinstance(x, (int, float)) for x in args)
    assert all(isinstance(x, str) for x in kwargs.values())


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    try:
        assert_types(args, kwargs)
        sorted_args = sorted(args)
        print(sorted_args)

        mean = ft_mean(sorted_args)
        print(f"mean: {mean}")
        median = ft_median(sorted_args)
        print(f"median: {median}")
        iqr1 = ft_interquartile(sorted_args)
        print(f"interquartile1: {iqr1}")
        std = ft_std(var)
        print(f"std: {std}")
        var = ft_var(sorted_args, mean)
        print(f"var: {var}")


    except Exception as e:
        print(f"ERROR")


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
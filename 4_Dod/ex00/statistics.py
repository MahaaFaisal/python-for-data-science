from math import sqrt


def ft_mean(args: int | float) -> float:
    return sum(args) / len(args)


def ft_var(args: int | float) -> float:
    mean = ft_mean(args)
    args = tuple(((x - mean)**2 for x in args))
    return sum(args) / len(args)


def ft_std(args: int | float) -> float:
    var = ft_var(args)
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
    i3 = ((75 / 100) * (n))

    return [float(args[int(i1)]), float(args[int(i3)])]

def assert_types(args: tuple[int | float], kwargs: dict[str]) -> None:
    assert all(isinstance(x, (int, float)) for x in args)
    assert all(isinstance(x, str) for x in kwargs.values())


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    functions = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_interquartile,
        "std": ft_std,
        "var": ft_var
    }

    try:
        assert_types(args, kwargs)
        sorted_args = sorted(args)
        for value in kwargs.values():
            try:
                if value in functions.keys():
                    print(f"{value} : {functions[value](sorted_args)}")
            except Exception:
                print("ERROR")

    except Exception as e:
        print(f"ERROR, {e}")


ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
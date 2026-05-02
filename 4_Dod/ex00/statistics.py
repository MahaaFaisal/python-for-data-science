from math import sqrt


def ft_mean(args: int | float) -> float:
    """Return the arithmetic mean of the given numeric values."""
    return sum(args) / len(args)


def ft_var(args: int | float) -> float:
    """Return the population variance of the given numeric values."""
    mean = ft_mean(args)
    args = tuple(((x - mean)**2 for x in args))
    return sum(args) / len(args)


def ft_std(args: int | float) -> float:
    """Return the population standard deviation of the given values."""
    var = ft_var(args)
    return sqrt(var)


def ft_median(args: int | float) -> float:
    """Return the median value from an ordered sequence of numbers."""
    n = len(args)
    mid_index = n // 2
    if (mid_index % 2 == 1):
        return (args[mid_index] + args[mid_index + 1]) / 2
    return args[mid_index]


def ft_interquartile(args: int | float) -> float:
    """Return the first and third quartile values as floats."""
    n = len(args)
    i1 = ((25 / 100) * (n))
    i3 = ((75 / 100) * (n))

    return [float(args[int(i1)]), float(args[int(i3)])]


def assert_types(args: tuple[int | float], kwargs: dict[str]) -> None:
    """Validate that positional values are numeric and options are strings."""
    assert all(isinstance(x, (int, float)) for x in args)
    assert all(isinstance(x, str) for x in kwargs.values())


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    """Print requested statistics for the supplied numeric arguments."""
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

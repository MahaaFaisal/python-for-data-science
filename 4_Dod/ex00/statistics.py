from statistics import mean


def assert_types(*args: int | float, **kwargs: str) -> None:
    assert all(isinstance(x, (int, float)) for x in args)
    assert all(isinstance(x, str) for x in kwargs)


def ft_statistics(*args: int | float, **kwargs: str) -> None:
    try:
        assert_types(args, kwargs)
        print(mean(args))

    except Exception as e: 
        print(f"{type(e).__name__}: {e}")


ft_statistics(2, 3, 2, toto="mean")

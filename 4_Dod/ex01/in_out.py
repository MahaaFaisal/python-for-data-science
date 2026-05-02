
def square(x: int | float) -> int | float:
    """Return the square of a numeric value."""
    return x**2


def pow(x: int | float) -> int | float:
    """Return a numeric value raised to its own power."""
    return x**x


def outer(x: int | float, function) -> object:
    """Return a closure that repeatedly applies a function to a stored value."""
    count = 0

    def inner() -> float:
        """Apply the saved function once and return the updated value."""
        nonlocal x, count
        x = function(x)
        count += 1
        return x
    return inner


def show_cell_content(closure):
    """Print the contents of each cell in a closure."""
    for i in range(len(closure)):
        print(f"closure {i}: {closure[i].cell_contents}")

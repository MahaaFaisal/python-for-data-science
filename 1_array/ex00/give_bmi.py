

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
a function that takes a list of heights,\
and returns the corresponding bmi for each
    """
    if len(height) != len(weight):
        raise ValueError("Lists must be of the same length")
    if (not all(isinstance(x, (int, float)) for x in height)
            or not all(isinstance(x, (int, float)) for x in weight)):
        raise TypeError("List elements must be int or float")
    return list(map(lambda h, w: w / (h * h), height, weight))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
a function that takes a list of bmis and a limit and returns a list\
    of booleans wether that bmi is greater than limit or no
    """
    return list(map(lambda x: x > limit, bmi))

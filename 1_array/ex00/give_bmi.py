

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
Return a list of BMI values computed from heights and weights.

BMI is calculated as weight / (height * height) for each index.
    """

    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("height and weight should be lists")
    if len(height) != len(weight):
        raise ValueError("Lists must be of the same length")
    if (not all(isinstance(x, (int, float)) for x in height)
            or not all(isinstance(x, (int, float)) for x in weight)):
        raise TypeError("List elements must be int or float")
    return list(map(lambda h, w: w / (h * h), height, weight))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Return a list of booleans indicating whether each BMI exceeds the limit.
    """

    if not isinstance(bmi, list):
        raise ValueError("bmi should be a list")
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise TypeError("List elements must be int or float")
    return list(map(lambda x: x > limit, bmi))

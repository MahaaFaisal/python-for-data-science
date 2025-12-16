

def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Lists must be of the same length")
    return list(map(lambda h, w: w / (h * h), height, weight))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return list(map(lambda x: x > limit, bmi))

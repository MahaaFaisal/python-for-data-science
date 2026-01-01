import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
Slice a 2D list from start to end indices.
Raises a ValueError if the input is not a proper 2D list.
    """
    try:
        family_arr = np.asarray(family)
    except Exception:
        raise ValueError("cannot convert list to an array")

    if (family_arr.ndim != 2):
        raise ValueError("array should be 2D")

    print("My shape is :", family_arr.shape)
    slice_object = slice(start, end)
    sliced_family = family[slice_object]
    print("My new shape is :", np.asarray(sliced_family).shape)
    return sliced_family

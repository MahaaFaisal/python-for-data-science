import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    family_arr = np.asarray(family)
    print("My shape is :", np.asarray(family).shape)
    slice_object = slice(start, end)
    sliced_family = family[slice_object]
    print("My new shape is :", np.asarray(sliced_family).shape)
    return sliced_family

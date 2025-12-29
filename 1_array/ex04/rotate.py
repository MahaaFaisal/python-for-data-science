import numpy as np


def ft_rotate(image_arr: np.ndarray) -> np.ndarray:
    if (image_arr.ndim == 3):
        image_arr = image_arr[..., 0]

    rotated_arr = [list(row) for row in zip(*image_arr)]

    return np.array(rotated_arr)

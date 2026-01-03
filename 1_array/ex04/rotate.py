import numpy as np


def ft_rotate(image_arr: np.ndarray) -> np.ndarray:
    """Rotate a 2D image array by transposing it.
If the input is RGB, only the first channel is used.
"""
    try:
        if (image_arr.ndim == 3):
            image_arr = np.squeeze(image_arr)
        rotated_arr = [list(row) for row in zip(*image_arr)]
        return np.array(rotated_arr)
    except Exception:
        raise Exception("failed to rotate the image")

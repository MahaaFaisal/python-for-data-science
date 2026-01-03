from PIL import Image
import numpy as np


def ft_invert(image_arr: np.ndarray) -> np.ndarray:
    """Invert the colors of an image by subtracting pixel values from 255."""
    inverted_arr = 255 - image_arr
    Image.fromarray(inverted_arr).show()
    return inverted_arr


def ft_red(image_arr: np.ndarray) -> np.ndarray:
    """Keep only the red channel of an RGB image."""
    mask = np.array([1, 0, 0], dtype=image_arr.dtype)
    red_arr = image_arr * mask
    Image.fromarray(red_arr).show()
    return red_arr


def ft_green(image_arr: np.ndarray) -> np.ndarray:
    """Keep only the green channel of an RGB image."""
    copy_arr = image_arr.copy()
    copy_arr[:, :, 0] = copy_arr[:, :, 2] = 0
    Image.fromarray(copy_arr).show()
    return copy_arr


def ft_blue(image_arr: np.ndarray) -> np.ndarray:
    """Keep only the blue channel of an RGB image."""
    copy_arr = image_arr.copy()
    copy_arr[:, :, 0] = copy_arr[:, :, 1] = 0
    Image.fromarray(copy_arr).show()
    return copy_arr


def ft_grey(image_arr: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale using the mean of its channels."""
    copy_arr = image_arr.copy()

    copy_arr[:] = np.mean(copy_arr, axis=-1, keepdims=True)
    print(copy_arr.shape)

    Image.fromarray(copy_arr).show()
    return copy_arr

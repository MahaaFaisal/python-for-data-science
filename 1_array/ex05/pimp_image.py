from PIL import Image
import numpy as np


def ft_invert(image_arr: np.ndarray) -> np.ndarray:
    inverted_arr = 255 - image_arr
    # Image.fromarray(inverted_arr).show()
    return inverted_arr


def ft_red(image_arr: np.ndarray) -> np.ndarray:
    red_arr = image_arr[:, :, 0]
    Image.fromarray(red_arr).show()
    return red_arr


def ft_green(image_arr: np.ndarray) -> np.ndarray:
    return 255 - image_arr


def ft_blue(image_arr: np.ndarray) -> np.ndarray:
    return 255 - image_arr


def ft_grey(image_arr: np.ndarray) -> np.ndarray:
    return 255 - image_arr

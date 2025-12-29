from PIL import Image
import numpy as np


def ft_invert(image_arr: np.ndarray) -> np.ndarray:
    inverted_arr = 255 - image_arr
    Image.fromarray(inverted_arr).show()
    return inverted_arr


def ft_red(image_arr: np.ndarray) -> np.ndarray:
    copy_arr = image_arr.copy()
    copy_arr[:, :, 1] = copy_arr[:, :, 2] = 0
    Image.fromarray(copy_arr).show()
    return copy_arr


def ft_green(image_arr: np.ndarray) -> np.ndarray:
    copy_arr = image_arr.copy()
    copy_arr[:, :, 0] = copy_arr[:, :, 2] = 0
    Image.fromarray(copy_arr).show()
    return copy_arr


def ft_blue(image_arr: np.ndarray) -> np.ndarray:
    copy_arr = image_arr.copy()
    copy_arr[:, :, 0] = copy_arr[:, :, 1] = 0
    Image.fromarray(copy_arr).show()
    return copy_arr


def ft_grey(image_arr: np.ndarray) -> np.ndarray:
    copy_arr = image_arr.copy()

    copy_arr[:] = np.mean(copy_arr, axis=-1, keepdims=True)
    print(copy_arr.shape)

    Image.fromarray(copy_arr).show()
    return copy_arr

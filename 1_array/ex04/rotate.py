from PIL import Image
import numpy as np


def ft_rotate(image_arr: np.ndarray):
    rotated_arr = list(zip(*image_arr))
    
    return rotated_arr

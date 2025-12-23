from PIL import Image
import numpy as np


def ft_zoom(image_arr: np.ndarray, region: tuple[int, int, int, int]):
    image = Image.fromarray(image_arr)
    # zoom
    cropped = image.convert("L").crop(region)
    cropped_arr = np.asarray(cropped)
    cropped.show()
    print(f"New shape after slicing: {cropped_arr.shape}")

    # convert to luminance
    return cropped_arr

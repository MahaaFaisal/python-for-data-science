from PIL import Image
import numpy as np


def ft_zoom(image_arr: np.ndarray, region: tuple[int, int, int, int]):
    image = Image.fromarray(image_arr)

    cropped = image.convert("L").crop(region)
    cropped_arr = np.asarray(cropped)
    cropped_arr = cropped_arr[..., np.newaxis]

    cropped.show()
    print(f"The shape of image is: {cropped_arr.shape}")

    return cropped_arr

from PIL import Image
import numpy as np


def ft_zoom(image_arr: np.ndarray, region: tuple[int, int, int, int]):
    """
Crops the image and converts it to grayscale.
    """
    try:
        image = Image.fromarray(image_arr)
        # zoom
        cropped = image.convert("L").crop(region)
        cropped_arr = np.asarray(cropped)
        cropped_arr = cropped_arr[..., np.newaxis]

        cropped.show()
        print(f"New shape after slicing: {cropped_arr.shape}")
        return cropped_arr
    except Exception as e:
        raise Exception(f"failed to zoom image: {e}")

from load_image import ft_load
from zoom import ft_zoom
from rotate import ft_rotate
from PIL import Image
import numpy as np


def main():
    try:
        image_arr = ft_load("animal.jpeg")
        zoomed_arr = ft_zoom(image_arr, (450, 100, 850, 500))
        print(zoomed_arr)
        rotated_arr = ft_rotate(zoomed_arr)
        print(rotated_arr)
        Image.fromarray(rotated_arr).show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

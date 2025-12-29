from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:

        image = Image.open(path)
        image_array = np.asarray(image)

        print(f"The shape of the image is: {image_array.shape}")
        return image_array

    except OSError:
        raise OSError("Failed to open file")
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    except Exception as e:
        raise Exception(f"error loading image: {e}")
    finally:
        image.close()

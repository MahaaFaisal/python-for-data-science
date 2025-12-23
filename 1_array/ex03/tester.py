from load_image import ft_load
from zoom import ft_zoom


def main():
    try:
        image_arr = ft_load("animal.jpeg")
        print(image_arr)
        print(ft_zoom(image_arr, (450, 100, 850, 500)))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

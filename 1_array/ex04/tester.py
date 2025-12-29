from load_image import ft_load
from zoom import ft_zoom


def main():
    try:
        image_arr = ft_load("animal.jpeg")
        zoomed_arr = ft_zoom(image_arr, (450, 100, 850, 500))
        print(zoomed_arr)
        print(ft_rotate(zoomed_arr))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import sys


def main():
    try:
        image_arr = ft_load("landscape.jpg")
        ft_invert(image_arr)
        ft_red(image_arr)
        ft_green(image_arr)
        ft_blue(image_arr)
        ft_grey(image_arr)
        print(ft_invert.__doc__)

    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    main()

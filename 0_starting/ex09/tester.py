from ft_package import count_in_list


def main():
    try:
        print(count_in_list([3, 3, 1, 2, 3, 4], 3))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

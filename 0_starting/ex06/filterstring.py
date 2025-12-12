import sys
from ft_filter import ft_filter


def main():
    try:
        args = sys.argv
        if (len(args) != 3):
            raise AssertionError("AssertionError: the arguments are bad")

        string = "".join([c for c in args[1] if c.isalnum() or c.isspace()])
        n = int(args[2])

        x = ft_filter(lambda string: len(string) > n, string.split())
        print(list(x))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

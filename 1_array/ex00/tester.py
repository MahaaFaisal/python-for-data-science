from give_bmi import give_bmi, apply_limit
import sys


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        if (bmi):
            print(bmi, type(bmi))
            print(apply_limit(bmi, 26))
    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == "__main__":
    main()

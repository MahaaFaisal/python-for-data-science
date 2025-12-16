import sys


def string_to_morse(string: str):
    """ function that takes a string as an argument and returns
    its morse code translation

    str -- the alphabetical string to convert

    """
    NESTED_MORSE = {"A": ".-",      "B": "-...",
                    "C": "-.-.",    "D": "-..",    "E": ".",
                    "F": "..-.",    "G": "--.",     "H": "....",
                    "I": "..",      "J": ".---",    "K": "-.-",
                    "L": ".-..",    "M": "--",      "N": "-.",
                    "O": "---",     "P": ".--.",    "Q": "--.-",
                    "R": ".-.",     "S": "...",     "T": "-",
                    "U": "..-",     "V": "...-",    "W": ".--",
                    "X": "-..-",    "Y": "-.--",    "Z": "--..",
                    "1": ".----",   "2": "..---",   "3": "...--",
                    "4": "....-",   "5": ".....",   "6": "-....",
                    "7": "--...",   "8": "---..",   "9": "----.",
                    "0": "-----",   " ": "/"}
    return (" ".join([NESTED_MORSE[c] for c in string.upper()]))


def main():
    try:
        args = sys.argv
        if (len(args) != 2 or
           not all(x.isalnum() or x == " " for x in args[1])):
            raise AssertionError("AssertionError: the arguments are bad")
        print(string_to_morse(args[1]))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
